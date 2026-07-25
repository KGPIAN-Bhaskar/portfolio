import os
import json
import urllib.request
import urllib.parse
from datetime import datetime
import streamlit as st

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


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
    # 1. Fetch Apps Script URL from environment or Streamlit secrets
    script_url = os.getenv("GOOGLE_APPS_SCRIPT_URL", "").strip()
    if not script_url and hasattr(st, "secrets") and "GOOGLE_APPS_SCRIPT_URL" in st.secrets:
        script_url = st.secrets["GOOGLE_APPS_SCRIPT_URL"].strip()

    # 2. Check if URL is unconfigured or placeholder
    if not script_url or "YOUR_SCRIPT_ID" in script_url:
        return (
            False,
            "Google Apps Script URL is missing in `.env`. Please add `GOOGLE_APPS_SCRIPT_URL` to enable Google Sheets & Email notification."
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
                "User-Agent": "Mozilla/5.0"
            },
            method="POST"
        )
        
        with urllib.request.urlopen(req, timeout=12) as response:
            resp_bytes = response.read()
            resp_str = resp_bytes.decode("utf-8")
            
            # Check JSON result if returned
            try:
                resp_json = json.loads(resp_str)
                if resp_json.get("result") == "error":
                    return (False, f"Processing error: {resp_json.get('error', 'Unknown error')}")
            except Exception:
                pass
                
            return (True, "Thank you! Your message has been saved to Google Sheets and emailed to mandalbhaskar540@gmail.com.")
            
    except Exception as e:
        return (False, f"Submission error: {str(e)}. Please check your connection and try again.")
