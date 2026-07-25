from typing import Optional, Callable
import streamlit as st

def render_section_header(
    title: str,
    subtitle: Optional[str] = None,
    badge: Optional[str] = None,
    section_id: Optional[str] = None
) -> None:
    """
    Renders a standardized, high-aesthetic section header with optional badge and anchor ID.
    """
    anchor_html = f'<div id="{section_id}" style="position: relative; top: -60px;"></div>' if section_id else ""
    badge_html = f'<div class="section-badge">{badge}</div>' if badge else ""
    subtitle_html = f'<p class="section-subtitle">{subtitle}</p>' if subtitle else ""
    
    header_html = f"""{anchor_html}
<div class="section-header">
{badge_html}
<h2 class="section-title">{title}</h2>
{subtitle_html}
</div>"""
    st.markdown(header_html, unsafe_allow_html=True)


def render_section(
    title: str,
    subtitle: Optional[str] = None,
    badge: Optional[str] = None,
    section_id: Optional[str] = None,
    content_fn: Optional[Callable[[], None]] = None
) -> None:
    """
    Renders a complete, modular portfolio section wrapper.
    """
    st.markdown('<div class="portfolio-section">', unsafe_allow_html=True)
    render_section_header(title=title, subtitle=subtitle, badge=badge, section_id=section_id)
    
    if content_fn:
        content_fn()
        
    st.markdown('</div>', unsafe_allow_html=True)
