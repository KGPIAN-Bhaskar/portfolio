import os
import base64
import json
import streamlit as st
from utils.html_render import render_html

@st.cache_data
def get_kit_pdf_base64(pdf_path: str) -> str:
    """
    Converts a local PDF file to base64 string for direct inline download/preview.
    Cached for fast rendering performance.
    """
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as pdf_file:
            return base64.b64encode(pdf_file.read()).decode("utf-8")
    return ""


@st.cache_data
def load_interview_kits_data() -> dict:
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


def render_interview_kits():
    """
    Renders the Interview Kits section with 4 large premium cards loaded from JSON.
    """
    kits_data = load_interview_kits_data()
    kits = kits_data.get("interview_kits", [])
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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

    # Build Cards HTML
    cards_html_list = []
    for kit in kits:
        k_icon = kit.get("icon", "📚")
        k_title = kit.get("title", "")
        k_file = kit.get("file", "")
        k_topics = kit.get("topics", [])

        # Build Base64 Data URI for PDF
        pdf_path = os.path.join(base_dir, k_file.replace("/", os.sep))
        pdf_b64 = get_kit_pdf_base64(pdf_path)
        pdf_href = f"data:application/pdf;base64,{pdf_b64}" if pdf_b64 else "#"

        # Build Topic Tags HTML
        topics_html = "".join([f'<span class="kit-topic-tag">• {topic}</span>' for topic in k_topics])

        filename = os.path.basename(k_file)

        card_html = f"""
        <div class="interview-kit-card">
            <div class="kit-header">
                <div class="kit-icon">{k_icon}</div>
                <h3 class="kit-title">{k_title}</h3>
            </div>
            
            <div class="kit-topics-container">
                {topics_html}
            </div>
            
            <div class="kit-actions">
                <a href="{pdf_href}" target="_blank" class="kit-btn-preview" title="Preview PDF">
                    👁️ Preview
                </a>
                <a href="{pdf_href}" download="{filename}" class="kit-btn-download" title="Download PDF">
                    📥 Download PDF
                </a>
            </div>
        </div>
        """
        cards_html_list.append(card_html)

    all_cards_html = "".join(cards_html_list)
    grid_html = f"""
    <div class="interview-kits-grid">
        {all_cards_html}
    </div>
    """
    render_html(grid_html)
