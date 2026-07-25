import os
import base64
import streamlit as st
from data.profile_data import PROFILE_DATA
from utils.html_render import render_html

def get_image_base64(image_path: str) -> str:
    """
    Converts local image file to base64 string for embedding.
    """
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    return ""

def render_hero():
    """
    Renders the Home / Hero section component.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    img_path = os.path.join(base_dir, "assets", "profile.png")
    img_b64 = get_image_base64(img_path)
    
    avatar_src = f"data:image/png;base64,{img_b64}" if img_b64 else "https://via.placeholder.com/170"

    # SVG Icons for GitHub, LinkedIn, Email, Intern Verification, Google Badge
    github_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"></path><path d="M9 18c-4.51 2-5-2-7-2"></path></svg>"""
    linkedin_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>"""
    email_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>"""
    verify_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path><path d="m9 12 2 2 4-4"></path></svg>"""
    badge_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="6"></circle><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"></path></svg>"""

    badges_html = "".join([f'<span class="hero-badge-pill">{badge}</span>' for badge in PROFILE_DATA["skills_badges"]])

    hero_html = f"""
    <div id="home" class="hero-card">
        <div class="hero-avatar-container">
            <div class="hero-avatar-wrapper">
                <img src="{avatar_src}" alt="{PROFILE_DATA['name']}" class="hero-avatar-img" />
            </div>
        </div>
        <h1 class="hero-name">{PROFILE_DATA['name']}</h1>
        <div class="university-tag">
            🎓 {PROFILE_DATA['university']} (M.Tech CSE '27)
        </div>
        <div class="hero-badges-container">
            {badges_html}
        </div>
        <p class="hero-bio">
            {PROFILE_DATA['tagline']}
        </p>
        <div class="hero-cta-container">
            <a href="#projects" class="btn-primary">
                🚀 Explore Projects
            </a>
            <a href="#contact" class="btn-secondary">
                ✉️ Contact Me
            </a>
        </div>
        <div class="hero-social-container">
            <a href="{PROFILE_DATA['social']['github']}" target="_blank" rel="noopener noreferrer" class="social-icon-btn" title="GitHub Profile">
                {github_svg}
            </a>
            <a href="{PROFILE_DATA['social']['linkedin']}" target="_blank" rel="noopener noreferrer" class="social-icon-btn" title="LinkedIn Profile">
                {linkedin_svg}
            </a>
            <a href="{PROFILE_DATA['social']['email']}" class="social-icon-btn" title="Send Email">
                {email_svg}
            </a>
            <a href="{PROFILE_DATA['social']['intern_verify']}" target="_blank" rel="noopener noreferrer" class="social-icon-btn" title="Internship Verification Portfolio">
                {verify_svg}
            </a>
            <a href="{PROFILE_DATA['social']['google_badge']}" target="_blank" rel="noopener noreferrer" class="social-icon-btn" title="Google Certified Badge (Credly)">
                {badge_svg}
            </a>
        </div>
    </div>
    """
    render_html(hero_html)
