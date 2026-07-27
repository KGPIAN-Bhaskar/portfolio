import os
import base64
import json
import streamlit as st
from utils.html_render import render_html

@st.cache_data
def get_project_image_base64(image_path: str, mtime: float = 0) -> str:
    """
    Converts a local image file to a base64 encoded string for inline HTML rendering.
    Cached for fast rendering performance, invalidated when file mtime changes.
    """
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    return ""


@st.cache_data
def load_projects_data() -> dict:
    """
    Safely loads project records from data/projects.json.
    Cached for fast rendering performance.
    """
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(base_dir, "data", "projects.json")
        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        st.error(f"Error loading projects.json: {str(e)}")
    return {"projects": []}


def render_projects():
    """
    Renders the Featured Projects section with reusable glass cards loaded from JSON.
    """
    projects_data = load_projects_data()
    projects = projects_data.get("projects", [])
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Anchored Section Title Header
    header_html = """
    <div id="projects" style="position: relative; top: -60px;"></div>
    <div class="about-header-container">
        <h2 class="about-main-title">FEATURED <span class="about-title-highlight">PROJECTS</span></h2>
        <div class="about-title-underline"></div>
    </div>
    """
    render_html(header_html)

    # Build Project Cards HTML
    cards_html_list = []
    for proj in projects:
        p_title = proj.get("title", "")
        p_category = proj.get("category", "")
        p_desc = proj.get("description", "")
        p_highlight = proj.get("highlight", "")
        p_tech = proj.get("tags", proj.get("tech_stack", []))
        p_img_rel = proj.get("image", "")
        p_github = proj.get("github", proj.get("github_url", "#"))
        p_demo = proj.get("demo", proj.get("demo_url", "#"))

        # Encode local cover image to base64 (busting cache when file mtime changes)
        img_path = os.path.join(base_dir, p_img_rel.replace("/", os.sep))
        mtime = os.path.getmtime(img_path) if os.path.exists(img_path) else 0
        img_b64 = get_project_image_base64(img_path, mtime)
        img_src = f"data:image/png;base64,{img_b64}" if img_b64 else "https://via.placeholder.com/600x350/0f172a/00f5d4?text=Project+Thumbnail"

        # Build Tech Stack Pills HTML
        tech_html = "".join([f'<span class="project-tag">{t}</span>' for t in p_tech])

        card_html = f"""
        <div class="project-card">
            <div class="project-img-wrapper">
                <img src="{img_src}" alt="{p_title}" loading="lazy" decoding="async" />
                <span class="project-category-badge">{p_category}</span>
            </div>
            
            <div class="project-content">
                <h3 class="project-title">{p_title}</h3>
                <div class="project-highlight">⚡ {p_highlight}</div>
                <p class="project-description">{p_desc}</p>
                
                <div class="project-tech-tags">
                    {tech_html}
                </div>
                
                <div class="project-actions">
                    <a href="{p_github}" target="_blank" rel="noopener noreferrer" class="project-btn-github" title="View Code on GitHub">
                        <span>💻 Code</span>
                    </a>
                    <a href="{p_demo}" target="_blank" rel="noopener noreferrer" class="project-btn-demo" title="Open Live Streamlit App">
                        <span>🚀 Live Demo</span>
                    </a>
                </div>
            </div>
        </div>
        """
        cards_html_list.append(card_html)

    all_cards_html = "".join(cards_html_list)
    grid_html = f"""
    <div class="projects-grid">
        {all_cards_html}
    </div>
    """
    render_html(grid_html)
