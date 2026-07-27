import os
import base64
import json
import logging
from typing import Dict, Any
import streamlit as st

logger = logging.getLogger(__name__)


@st.cache_data
def load_cached_base64(file_path: str, mtime: float = 0.0) -> str:
    """
    Converts a local file (e.g. image or PDF) to a base64 encoded string.
    Cached using @st.cache_data for instant rendering performance.

    Args:
        file_path (str): Absolute or relative path to the target file.
        mtime (float, optional): File modification timestamp for cache-busting.

    Returns:
        str: Base64 string if file exists and is readable, else empty string.
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                return base64.b64encode(f.read()).decode("utf-8")
        logger.warning("Base64 target file not found: %s", file_path)
    except Exception as e:
        logger.error("Error reading base64 file '%s': %s", file_path, str(e))
    return ""


@st.cache_data
def load_cached_binary(file_path: str, mtime: float = 0.0) -> bytes:
    """
    Reads and caches binary data from a file (e.g. PDF documents).

    Args:
        file_path (str): Path to the binary file.
        mtime (float, optional): File modification timestamp for cache invalidation.

    Returns:
        bytes: Raw bytes if file exists, else empty bytes.
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                return f.read()
        logger.warning("Binary target file not found: %s", file_path)
    except Exception as e:
        logger.error("Error reading binary file '%s': %s", file_path, str(e))
    return b""


@st.cache_data
def load_cached_json(file_path: str, mtime: float = 0.0) -> Dict[str, Any]:
    """
    Reads and caches structured JSON data from disk.

    Args:
        file_path (str): Path to the JSON file.
        mtime (float, optional): File modification timestamp for cache invalidation.

    Returns:
        dict: Parsed JSON object, or empty dict if file fails to load.
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        logger.warning("JSON target file not found: %s", file_path)
    except Exception as e:
        logger.error("Error reading JSON file '%s': %s", file_path, str(e))
    return {}
