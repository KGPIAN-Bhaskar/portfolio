import os
import streamlit as st
from utils.html_render import render_html
from utils.asset_loader import load_cached_json


def render_interview_kits():
    """
    Renders the Interview Kits section with 4 large premium cards loaded from JSON.
    Each card displays its price label and a direct link button to purchase via Topmate.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, "data", "interview_kits.json")
    json_mtime = os.path.getmtime(json_path) if os.path.exists(json_path) else 0

    kits_data = load_cached_json(json_path, json_mtime)
    kits = kits_data.get("interview_kits", [])

    # Anchored Section Title Header
    header_html = """
    <div id="kits" style="position: relative; top: -60px;"></div>
    <div class="about-header-container">
        <h2 class="about-main-title">INTERVIEW <span class="about-title-highlight">KITS</span></h2>
        <div class="about-title-underline"></div>
        <p style="color: #94a3b8; font-size: 1.05rem; max-width: 680px; margin: 1rem auto 0 auto; line-height: 1.6;">
            Curated interview preparation resources for AI, Machine Learning, Data Science, and Software Engineering.
        </p>
    </div>
    """
    render_html(header_html)

    # Custom CSS targeting Streamlit price & link buttons to match portfolio design
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
    div[data-testid="stColumn"] div[data-testid="stDownloadButton"] button,
    div[data-testid="stColumn"] div[data-testid="stLinkButton"] a {
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
        text-align: center !important;
        text-decoration: none !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    div[data-testid="stColumn"] div[data-testid="stDownloadButton"] button:hover,
    div[data-testid="stColumn"] div[data-testid="stLinkButton"] a:hover {
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
        k_topics = kit.get("topics", [])

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

            if k_id == "kit-ds":
                with b_col1:
                    st.button("₹99/-", key=f"price_btn_{k_id}_{idx}", use_container_width=True)

                with b_col2:
                    st.link_button(
                        "Buy Now",
                        "https://topmate.io/bhaskar_mandal/2230172",
                        use_container_width=True,
                        key=f"buy_now_btn_{k_id}_{idx}"
                    )
            elif k_id == "kit-dsa":
                with b_col1:
                    st.button("₹99/-", key=f"price_btn_{k_id}_{idx}", use_container_width=True)

                with b_col2:
                    st.link_button(
                        "Buy Now",
                        "https://topmate.io/bhaskar_mandal/2233687",
                        use_container_width=True,
                        key=f"buy_now_btn_{k_id}_{idx}"
                    )
            elif k_id == "kit-genai":
                with b_col1:
                    st.button("₹149/-", key=f"price_btn_{k_id}_{idx}", use_container_width=True)

                with b_col2:
                    st.link_button(
                        "Buy Now",
                        "https://topmate.io/bhaskar_mandal/2233764",
                        use_container_width=True,
                        key=f"buy_now_btn_{k_id}_{idx}"
                    )
            elif k_id == "kit-ml":
                with b_col1:
                    st.button("₹99/-", key=f"price_btn_{k_id}_{idx}", use_container_width=True)

                with b_col2:
                    st.link_button(
                        "Buy Now",
                        "https://topmate.io/bhaskar_mandal/2233767",
                        use_container_width=True,
                        key=f"buy_now_btn_{k_id}_{idx}"
                    )

            # Spacing below card
            render_html('<div style="margin-bottom: 1.75rem;"></div>')
