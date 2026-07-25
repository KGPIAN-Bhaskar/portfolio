import os
import base64
import streamlit as st
from data.profile_data import PROFILE_DATA
from utils.html_render import render_html

def get_image_base64(image_path: str) -> str:
    """
    Converts a local image file to base64 for embedding inside HTML.
    """
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    return ""


def render_about():
    """
    Renders the About Me section matching the reference design.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    img_path = os.path.join(base_dir, "assets", "profile.png")
    pdf_path = os.path.join(base_dir, "Bhaskar_Mandal_Gen_AI_Engineer_25_july.pdf")
    
    img_b64 = get_image_base64(img_path)
    avatar_src = f"data:image/png;base64,{img_b64}" if img_b64 else "https://via.placeholder.com/170"

    # SVG Icons
    user_icon_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>"""
    building_icon_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="20" x="4" y="2" rx="2" ry="2"></rect><path d="M9 22v-4h6v4"></path><path d="M8 6h.01"></path><path d="M16 6h.01"></path><path d="M12 6h.01"></path><path d="M12 10h.01"></path><path d="M16 10h.01"></path><path d="M16 14h.01"></path><path d="M8 10h.01"></path><path d="M8 14h.01"></path></svg>"""
    award_icon_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="6"></circle><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"></path></svg>"""
    calendar_icon_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect><line x1="16" x2="16" y1="2" y2="6"></line><line x1="8" x2="8" y1="2" y2="6"></line><line x1="3" x2="21" y1="10" y2="10"></line></svg>"""
    code_icon_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>"""

    # Section Title Header
    header_html = """
    <div id="about" style="position: relative; top: -60px;"></div>
    <div class="about-header-container">
        <h2 class="about-main-title">ABOUT <span class="about-title-highlight">ME</span></h2>
        <div class="about-title-underline"></div>
    </div>
    """
    render_html(header_html)

    # Top Overview Card
    overview_card_html = f"""
    <div class="about-card" style="text-align: center; margin-bottom: 2rem;">
        <div class="hero-avatar-container">
            <div class="hero-avatar-wrapper">
                <img src="{avatar_src}" alt="{PROFILE_DATA['name']}" class="hero-avatar-img" />
            </div>
        </div>
        <h3 style="font-size: 1.75rem; font-weight: 700; margin-bottom: 0.35rem; color: #ffffff;">{PROFILE_DATA['name']}</h3>
        <div style="color: #00f5d4; font-family: 'Fira Code', monospace; font-size: 0.95rem; font-weight: 600; margin-bottom: 1rem;">
            🏢 {PROFILE_DATA['university']}
        </div>
        <div class="hero-badges-container">
            <span class="hero-badge-pill">M.Tech CSE (2027)</span>
            <span class="hero-badge-pill">Generative AI</span>
            <span class="hero-badge-pill">RAG & Multi-Agent</span>
            <span class="hero-badge-pill">Python & PyTorch</span>
        </div>
    </div>
    """
    render_html(overview_card_html)

    # Detailed Professional Profile Card
    bio_text = "I'm a Master's student in Computer Science & Data Processing at IIT Kharagpur, passionate about building advanced Generative AI architectures and intelligent data systems. Over the past several months, I've developed end-to-end AI applications leveraging LLMs, vector databases (ChromaDB), computer vision pipelines (MediaPipe/OpenCV), and deep learning models (CNNs/TensorFlow). My goal is to launch my career as a Generative AI Engineer where I can drive innovation and solve high-impact real-world challenges."
    
    objective_text = "Looking for an opportunity as a Generative AI Engineer / Data Scientist where I can apply my technical knowledge in LLMs, RAG, and agent orchestration, gain hands-on industry experience, and build state-of-the-art AI applications."

    profile_card_html = f"""
    <div class="about-card">
        <div class="profile-section-header">
            <div class="profile-icon-badge">
                {user_icon_svg}
            </div>
            <div class="profile-title-group">
                <h3>Professional Profile</h3>
                <span>Computer Science | Generative AI & Data Processing</span>
            </div>
        </div>

        <p class="about-paragraph">
            {bio_text}
        </p>

        <div class="career-objective-box">
            <div class="objective-label">🎯 CAREER OBJECTIVE</div>
            <p class="objective-text">{objective_text}</p>
        </div>

        <div class="stat-grid">
            <div class="stat-card">
                <div class="stat-icon">{building_icon_svg}</div>
                <div class="stat-value">IIT Kharagpur</div>
                <div class="stat-label">University / Institution</div>
            </div>

            <div class="stat-card">
                <div class="stat-icon">{award_icon_svg}</div>
                <div class="stat-value">7.33 / 10</div>
                <div class="stat-label">M.Tech Academic CGPA</div>
            </div>

            <div class="stat-card">
                <div class="stat-icon">{calendar_icon_svg}</div>
                <div class="stat-value">2027</div>
                <div class="stat-label">Expected Graduation</div>
            </div>

            <div class="stat-card">
                <div class="stat-icon">{code_icon_svg}</div>
                <div class="stat-value">4+</div>
                <div class="stat-label">Major AI Projects Completed</div>
            </div>
        </div>
    </div>
    """
    render_html(profile_card_html)

    # Resume Download Bar
    col1, col2 = st.columns([2, 1])
    with col1:
        render_html('<div class="cv-status-text">📄 Curriculum Vitae Ready for Review</div>')
    with col2:
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as pdf_file:
                st.download_button(
                    label="📥 Download Resume",
                    data=pdf_file.read(),
                    file_name="Bhaskar_Mandal_Gen_AI_Engineer.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
