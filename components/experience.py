import os
from utils.html_render import render_html
from utils.asset_loader import load_cached_json


def render_experience() -> None:
    """
    Renders the Work Experience section with a vertical animated glass timeline loaded from JSON.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, "data", "experience.json")
    json_mtime = os.path.getmtime(json_path) if os.path.exists(json_path) else 0.0

    exp_data = load_cached_json(json_path, json_mtime)
    experiences = exp_data.get("experiences", [])

    # Anchored Section Title Header
    header_html = """
    <div id="experience" style="position: relative; top: -60px;"></div>
    <div class="about-header-container">
        <h2 class="about-main-title">WORK <span class="about-title-highlight">EXPERIENCE</span></h2>
        <div class="about-title-underline"></div>
    </div>
    """
    render_html(header_html)

    # Build Timeline Items HTML
    items_html_list = []
    for exp in experiences:
        e_role = exp.get("role", "")
        e_org = exp.get("organization", "")
        e_period = exp.get("period", "")
        e_type = exp.get("type", "Internship")
        e_icon = exp.get("icon", "💼")
        e_bullets = exp.get("bullets", [])
        e_skills = exp.get("skills", [])

        # Build Bullet Points HTML
        bullets_html = "".join([f'<li class="timeline-bullet-item">{bullet}</li>' for bullet in e_bullets])

        # Build Skill Tags HTML
        skills_html = "".join([f'<span class="timeline-skill-tag">{skill}</span>' for skill in e_skills])

        item_html = f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-card">
                <div class="timeline-header">
                    <div class="timeline-role-group">
                        <h3 class="timeline-role">{e_role}</h3>
                        <div class="timeline-org">
                            <span>{e_icon}</span> {e_org}
                        </div>
                    </div>
                    <div class="timeline-meta">
                        <span class="timeline-period">📅 {e_period}</span>
                        <span class="timeline-type-tag">⚡ {e_type}</span>
                    </div>
                </div>
                
                <ul class="timeline-bullets">
                    {bullets_html}
                </ul>
                
                <div class="timeline-skills-container">
                    {skills_html}
                </div>
            </div>
        </div>
        """
        items_html_list.append(item_html)

    all_timeline_items = "".join(items_html_list)
    timeline_wrapper_html = f"""
    <div class="timeline-wrapper">
        {all_timeline_items}
    </div>
    """
    render_html(timeline_wrapper_html)
