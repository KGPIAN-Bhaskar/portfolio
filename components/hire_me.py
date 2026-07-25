import os
import base64
import streamlit as st
from utils.html_render import render_html

@st.cache_data
def get_pdf_base64(pdf_path: str) -> str:
    """
    Converts a local PDF file to a base64 encoded string for direct inline download.
    Cached for fast rendering performance.
    """
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as pdf_file:
            return base64.b64encode(pdf_file.read()).decode("utf-8")
    return ""


def render_hire_me():
    """
    Renders Phase 9 Hire Me feature:
    1. Floating bottom-right action button (desktop only) linking to #contact with pulse glow animation.
    2. Premium pre-contact CTA card with availability status pills and resume download.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pdf_path = os.path.join(base_dir, "assets", "resume.pdf")
    if not os.path.exists(pdf_path):
        pdf_path = os.path.join(base_dir, "Bhaskar_Mandal_Gen_AI_Engineer_25_july.pdf")

    pdf_b64 = get_pdf_base64(pdf_path)
    resume_href = f"data:application/pdf;base64,{pdf_b64}" if pdf_b64 else "#"

    # 1. Floating Hire Me Button (Desktop Only)
    floating_btn_html = """
    <a href="#contact" class="floating-hire-btn" title="Hire Me - Scroll to Contact">
        ⚡ Hire Me
    </a>
    """
    render_html(floating_btn_html)

    # 2. Pre-Contact Call-to-Action Card
    cta_card_html = f"""
    <div id="hire-me" class="hire-cta-card">
        <h2 class="hire-cta-heading">Let's Build Something Amazing Together</h2>
        <p class="hire-cta-subheading">
            I'm actively seeking Full-Time opportunities in AI/ML Engineering, GenAI, NLP/LLM Engineering, Data Science, and Software Engineering. If you have an opportunity or project, I'd love to connect.
        </p>
        
        <div class="hire-availability-grid">
            <div class="hire-pill-card">
                <span class="hire-pill-icon">💼</span>
                <span>Open to Full-Time Roles</span>
            </div>
            <div class="hire-pill-card">
                <span class="hire-pill-icon">🚀</span>
                <span>Available for Freelance</span>
            </div>
            <div class="hire-pill-card">
                <span class="hire-pill-icon">🔬</span>
                <span>Research Collaboration</span>
            </div>
            <div class="hire-pill-card">
                <span class="hire-pill-icon">🌐</span>
                <span>Remote / Hybrid / Onsite</span>
            </div>
        </div>
        
        <div class="hire-btn-container">
            <a href="#contact" class="btn-primary">
                ⚡ Hire Me Now
            </a>
            <a href="{resume_href}" download="Bhaskar_Mandal_Resume.pdf" class="btn-secondary download-resume-btn">
                📄 Download Resume
            </a>
        </div>
    </div>
    """
    render_html(cta_card_html)
