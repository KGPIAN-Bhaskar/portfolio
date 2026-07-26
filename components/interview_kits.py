import os
import base64
import json
import streamlit as st
from utils.html_render import render_html

@st.cache_data
def get_kit_file_base64(file_path: str, mtime: float = 0) -> str:
    """
    Converts a local file (PDF) to base64 string for direct inline download.
    Cached for fast rendering performance, automatically invalidating when the file is updated.
    """
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""


@st.cache_data
def load_interview_kits_data(mtime: float = 0) -> dict:
    """
    Safely loads interview prep kit metadata from data/interview_kits.json.
    Cached using @st.cache_data for instant rendering performance.
    """
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(base_dir, "data", "interview_kits.json")
        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        st.error(f"Error loading interview_kits.json: {str(e)}")
    return {"interview_kits": []}


# Streamlit native modal dialog for image preview
if hasattr(st, "dialog"):
    @st.dialog("📄 Interview Kit Image Preview", width="large")
    def show_kit_preview_dialog(title: str, img_path: str):
        st.markdown(f"### {title}")
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.warning("Preview image file not found on server.")
else:
    def show_kit_preview_dialog(title: str, img_path: str):
        st.info(f"Previewing: {title}")
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)


def render_interview_kits():
    """
    Renders the Interview Kits section with 4 large premium cards loaded from JSON.
    - Preview button: native Streamlit button triggering dialog modal with image format.
    - Download PDF button: direct PDF download link.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, "data", "interview_kits.json")
    json_mtime = os.path.getmtime(json_path) if os.path.exists(json_path) else 0

    kits_data = load_interview_kits_data(json_mtime)
    kits = kits_data.get("interview_kits", [])

    # Anchored Section Title Header
    header_html = """
    <div id="kits" style="position: relative; top: -60px;"></div>
    <div class="about-header-container">
        <h2 class="about-main-title">INTERVIEW <span class="about-title-highlight">KITS</span></h2>
        <div class="about-title-underline"></div>
        <p style="color: #94a3b8; font-size: 1.05rem; max-width: 680px; margin: 1rem auto 0 auto; line-height: 1.6;">
            Download curated interview preparation resources for AI, Machine Learning, Data Science, and Software Engineering.
        </p>
    </div>
    """
    render_html(header_html)

    # Custom CSS targeting Streamlit preview & download buttons to match portfolio design
    custom_btn_css = """
    <style>
    div[data-testid="stColumn"] div[data-testid="stButton"] button {
        background: rgba(30, 41, 59, 0.85) !important;
        border: 1px solid rgba(0, 245, 212, 0.35) !important;
        color: #f8fafc !important;
        border-radius: 9999px !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        padding: 0.55rem 1rem !important;
        transition: all 0.2s ease-in-out !important;
        width: 100% !important;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2) !important;
    }
    div[data-testid="stColumn"] div[data-testid="stButton"] button:hover {
        border-color: #00f5d4 !important;
        color: #00f5d4 !important;
        box-shadow: 0 0 20px rgba(0, 245, 212, 0.3) !important;
        transform: translateY(-2px) !important;
    }
    div[data-testid="stColumn"] div[data-testid="stDownloadButton"] button {
        background: linear-gradient(135deg, #00f5d4 0%, #00bbf9 100%) !important;
        border: none !important;
        color: #070a13 !important;
        border-radius: 9999px !important;
        font-weight: 700 !important;
        font-size: 0.85rem !important;
        padding: 0.55rem 1rem !important;
        transition: all 0.2s ease-in-out !important;
        width: 100% !important;
        box-shadow: 0 0 15px rgba(0, 245, 212, 0.3) !important;
    }
    div[data-testid="stColumn"] div[data-testid="stDownloadButton"] button:hover {
        box-shadow: 0 0 25px rgba(0, 245, 212, 0.6) !important;
        transform: translateY(-2px) !important;
        color: #070a13 !important;
    }
    </style>
    """
    render_html(custom_btn_css)

    # Build 2x2 Grid via Streamlit columns
    col1, col2 = st.columns(2, gap="medium")

    for idx, kit in enumerate(kits):
        k_id = kit.get("id", "")
        k_icon = kit.get("icon", "📚")
        k_title = kit.get("title", "")
        k_file = kit.get("file", "")
        k_preview_img = kit.get("preview_image", "")
        k_topics = kit.get("topics", [])

        pdf_path = os.path.join(base_dir, k_file.replace("/", os.sep))
        filename = os.path.basename(k_file)
        img_path = os.path.join(base_dir, k_preview_img.replace("/", os.sep))

        # Read binary PDF file for native Streamlit download
        pdf_bytes = b""
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as f:
                pdf_bytes = f.read()

        # Build Topic Tags HTML
        topics_html = "".join([f'<span class="kit-topic-tag">• {topic}</span>' for topic in k_topics])

        target_col = col1 if idx % 2 == 0 else col2

        with target_col:
            # Card Container
            card_html = f"""
            <div class="interview-kit-card" style="margin-bottom: 0px; border-bottom-left-radius: 0; border-bottom-right-radius: 0; border-bottom: none; padding-bottom: 1rem;">
                <div class="kit-header">
                    <div class="kit-icon">{k_icon}</div>
                    <h3 class="kit-title">{k_title}</h3>
                </div>
                <div class="kit-topics-container" style="margin-bottom: 0.5rem;">
                    {topics_html}
                </div>
            </div>
            """
            render_html(card_html)

            # Action Buttons Row
            b_col1, b_col2 = st.columns(2, gap="small")

            with b_col1:
                if st.button("👁️ Preview", key=f"preview_btn_{k_id}_{idx}", use_container_width=True):
                    show_kit_preview_dialog(k_title, img_path)

            with b_col2:
                st.download_button(
                    label="📥 Download PDF",
                    data=pdf_bytes,
                    file_name=filename,
                    mime="application/pdf",
                    key=f"download_btn_{k_id}_{idx}",
                    use_container_width=True
                )

            # Spacing below card
            render_html('<div style="margin-bottom: 1.75rem;"></div>')



