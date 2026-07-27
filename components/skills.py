import os
import json
import streamlit as st
from utils.html_render import render_html

@st.cache_data
def load_skills_data() -> dict:
    """
    Safely loads skills categories and item lists from data/skills.json.
    Cached using @st.cache_data for instant rendering performance.
    """
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(base_dir, "data", "skills.json")
        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        st.error(f"Error loading skills.json: {str(e)}")
    return {"categories": []}


def render_skills():
    """
    Renders the Technical Skills section with animated glass cards loaded dynamically from JSON.
    """
    skills_data = load_skills_data()
    categories = skills_data.get("categories", skills_data.get("skills_categories", []))

    # Anchored Section Title Header
    header_html = """
    <div id="skills" style="position: relative; top: -60px;"></div>
    <div class="about-header-container">
        <h2 class="about-main-title">TECHNICAL <span class="about-title-highlight">SKILLS</span></h2>
        <div class="about-title-underline"></div>
    </div>
    """
    render_html(header_html)

    # Build Skill Cards HTML
    cards_html_list = []
    for cat in categories:
        cat_title = cat.get("title", cat.get("category", ""))
        cat_icon = cat.get("icon", "⚡")
        cat_skills = cat.get("skills", [])
        cat_badge = cat.get("badge", f"{len(cat_skills)} Skills")

        # Build Skill Progress Bars HTML
        items_html_list = []
        for sk in cat_skills:
            sk_name = sk.get("name", "")
            sk_level = sk.get("level", 80)
            sk_tag = sk.get("tag", "Advanced")

            item_html = f"""
            <div class="skill-item-container">
                <div class="skill-item-header">
                    <span class="skill-name">{sk_name}</span>
                    <span class="skill-tag">{sk_tag}</span>
                </div>
                <div class="skill-progress-bar">
                    <div class="skill-progress-fill" style="width: {sk_level}%;"></div>
                </div>
            </div>
            """
            items_html_list.append(item_html)

        all_items_html = "".join(items_html_list)

        card_html = f"""
        <div class="skill-card">
            <div class="skill-category-header">
                <div class="category-title-wrapper">
                    <span class="category-icon">{cat_icon}</span>
                    <h3 class="category-title">{cat_title}</h3>
                </div>
                <span class="category-badge">{cat_badge}</span>
            </div>
            <div class="skill-items-list">
                {all_items_html}
            </div>
        </div>
        """
        cards_html_list.append(card_html)

    all_cards_html = "".join(cards_html_list)
    grid_html = f"""
    <div class="skills-grid">
        {all_cards_html}
    </div>
    """
    render_html(grid_html)
