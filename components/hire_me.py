import os
import streamlit as st
from utils.html_render import render_html

def render_hire_me():
    """
    Renders Phase 9 Hire Me feature:
    1. Floating bottom-right action button (desktop only) linking to #contact with pulse glow animation.
    2. Premium pre-contact CTA card with availability status pills and resume download.
    """
    # 1. Floating Hire Me Button (Desktop Only)
    floating_btn_html = """
    <a href="#contact" class="floating-hire-btn" title="Hire Me - Scroll to Contact">
        ⚡ Hire Me
    </a>
    """
    render_html(floating_btn_html)

    # 2. Pre-Contact Call-to-Action Card
    cta_card_html = """
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
            <a href="assets/resume.pdf" download="Bhaskar_Mandal_Resume.pdf" target="_blank" class="btn-secondary">
                📄 Download Resume
            </a>
        </div>
    </div>
    """
    render_html(cta_card_html)
