import os
from data.profile_data import PROFILE_DATA
from utils.html_render import render_html
from utils.asset_loader import load_cached_base64


def render_navbar() -> None:
    """
    Renders the fixed top glassmorphic navigation bar.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    img_path = os.path.join(base_dir, "assets", "profile.png")
    mtime = os.path.getmtime(img_path) if os.path.exists(img_path) else 0.0
    img_b64 = load_cached_base64(img_path, mtime)
    
    avatar_src = f"data:image/png;base64,{img_b64}" if img_b64 else "https://via.placeholder.com/40"
    
    navbar_html = f"""
    <nav class="nav-container">
        <a href="#home" class="nav-brand">
            <img src="{avatar_src}" alt="{PROFILE_DATA['name']}" class="nav-avatar" />
            <div class="nav-brand-text">
                <span class="nav-name">{PROFILE_DATA['name']}</span>
                <span class="nav-sub">{PROFILE_DATA['nav_subtitle']}</span>
            </div>
        </a>
        <div class="nav-links">
            <a href="#home" class="nav-link active">Home</a>
            <a href="#about" class="nav-link">About</a>
            <a href="#skills" class="nav-link">Skills</a>
            <a href="#projects" class="nav-link">Projects</a>
            <a href="#experience" class="nav-link">Experience</a>
            <a href="#kits" class="nav-link">Kits</a>
            <a href="#contact" class="nav-link">Contact</a>
        </div>
    </nav>
    """
    render_html(navbar_html)
