import os
import json
import ssl
import urllib.request
import urllib.parse
from datetime import datetime
import streamlit as st

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

DEFAULT_APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxsSNyhrxEixriP0Fs_JzuWg6TwNx33X5nityZg9OSA6UNbWSySdnM8C7KTW1pLqmopYA/exec"


def _format_apps_script_url(raw_val: str) -> str:
    """Formats a script URL or script ID into a valid execution endpoint."""
    raw_val = raw_val.strip()
    if not raw_val:
        return ""
    if raw_val.startswith("http://") or raw_val.startswith("https://"):
        return raw_val
    # Automatically convert plain Script ID into full Web App URL
    return f"https://script.google.com/macros/s/{raw_val}/exec"


def get_apps_script_url() -> str:
    """
    Robustly retrieves the Google Apps Script Web App URL from:
    1. Environment variables (.env or OS env)
    2. Streamlit secrets (st.secrets) - checking all common key variations and nested tables
    3. Embedded default deployment URL fallback
    """
    possible_keys = [
        "GOOGLE_APPS_SCRIPT_URL",
        "GOOGLE_APPS_SCRIPT_ID",
        "GOOGLE_APPS_SCRIPT",
        "APPS_SCRIPT_URL",
        "APPS_SCRIPT_ID",
        "GOOGLE_SHEET_URL",
        "GOOGLE_SHEETS_URL",
    ]

    # 1. Check OS Environment / .env
    for key in possible_keys:
        for k in [key, key.lower(), key.upper()]:
            val = os.getenv(k, "").strip()
            if val and "YOUR_SCRIPT_ID" not in val:
                return _format_apps_script_url(val)

    # 2. Check Streamlit Cloud Secrets (st.secrets)
    try:
        if hasattr(st, "secrets") and st.secrets:
            # Top-level keys check
            for key in possible_keys:
                for k in [key, key.lower(), key.upper()]:
                    if k in st.secrets:
                        val = st.secrets[k]
                        if isinstance(val, str) and val.strip() and "YOUR_SCRIPT_ID" not in val:
                            return _format_apps_script_url(val.strip())
                        elif isinstance(val, dict):
                            sub_val = val.get("url") or val.get("id") or val.get("exec")
                            if sub_val and isinstance(sub_val, str) and sub_val.strip() and "YOUR_SCRIPT_ID" not in sub_val:
                                return _format_apps_script_url(sub_val.strip())

            # Nested sections search in st.secrets (e.g., [google], [general], [secrets])
            for sec_key in st.secrets:
                try:
                    sec = st.secrets[sec_key]
                    if isinstance(sec, dict):
                        for key in possible_keys + ["url", "id", "exec"]:
                            for k in [key, key.lower(), key.upper()]:
                                if k in sec:
                                    val = sec[k]
                                    if isinstance(val, str) and val.strip() and "YOUR_SCRIPT_ID" not in val:
                                        return _format_apps_script_url(val.strip())
                except Exception:
                    pass
    except Exception:
        pass

    # 3. Embedded Default Fallback URL
    return DEFAULT_APPS_SCRIPT_URL


def send_to_google_sheets(name: str, email: str, subject: str, message: str) -> tuple[bool, str]:
    """
    Sends contact submission data to Google Sheets via Google Apps Script Web App,
    which appends the row to Google Sheets and automatically emails mandalbhaskar540@gmail.com.
    
    Args:
        name (str): Sender's name.
        email (str): Sender's email.
        subject (str): Message subject.
        message (str): Message body.
        
    Returns:
        tuple[bool, str]: (Success status, User feedback message)
    """
    # 1. Fetch Apps Script URL from env, secrets, or fallback
    script_url = get_apps_script_url()

    # 2. Check if URL is unconfigured or placeholder
    if not script_url or "YOUR_SCRIPT_ID" in script_url:
        return (
            False,
            "Google Apps Script URL / ID is missing. Please add `GOOGLE_APPS_SCRIPT_URL` or `GOOGLE_APPS_SCRIPT_ID` in your `.env` file or Streamlit Cloud Secrets (Advanced Settings)."
        )

    # 3. Construct Payload with Timestamp and Notification Recipient
    timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload = {
        "timestamp": timestamp_str,
        "name": name.strip(),
        "email": email.strip(),
        "subject": subject.strip(),
        "message": message.strip(),
        "notification_email": "mandalbhaskar540@gmail.com"
    }

    try:
        json_data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            script_url,
            data=json_data,
            headers={
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            },
            method="POST"
        )
        
        # Execute HTTP POST request with SSL verification fallback
        resp_bytes = None
        try:
            ctx = ssl.create_default_context()
            with urllib.request.urlopen(req, timeout=12, context=ctx) as response:
                resp_bytes = response.read()
        except Exception:
            ctx = ssl._create_unverified_context()
            with urllib.request.urlopen(req, timeout=12, context=ctx) as response:
                resp_bytes = response.read()

        if resp_bytes is not None:
            resp_str = resp_bytes.decode("utf-8")
            
            # Check JSON result if returned
            try:
                resp_json = json.loads(resp_str)
                if resp_json.get("result") == "error":
                    return (False, f"Processing error: {resp_json.get('error', 'Unknown error')}")
            except Exception:
                pass
                
            return (True, "Thank you! Your message has been saved to Google Sheets and emailed to mandalbhaskar540@gmail.com.")
        else:
            return (False, "No response received from Google Apps Script. Please try again.")
            
    except Exception as e:
        return (False, f"Submission error: {str(e)}. Please check your connection and try again.")

