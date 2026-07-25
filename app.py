import streamlit as st
from utils.css_loader import load_css
from utils.analytics import inject_ga4
from components.navbar import render_navbar
from components.hero import render_hero
from components.about import render_about
from components.skills import render_skills
from components.projects import render_projects
from components.experience import render_experience
from components.interview_kits import render_interview_kits
from components.hire_me import render_hire_me
from components.contact import render_contact

# 1. Page Configuration
st.set_page_config(
    page_title="Bhaskar Mandal | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Inject Design System & Dark Glassmorphism CSS
load_css("styles/main.css")


def main():
    # Phase 10: Google Analytics 4 Silent Injection
    inject_ga4()
    
    # Fixed Top Glassmorphic Navigation Bar
    render_navbar()
    
    # Phase 1: Home / Hero Section
    render_hero()
    
    # Phase 2: About Me Section
    render_about()
    
    # Phase 3: Technical Skills Section
    render_skills()
    
    # Phase 4: Featured Projects Section
    render_projects()
    
    # Phase 5: Work Experience Section
    render_experience()
    
    # Phase 9: Interview Kits Section
    render_interview_kits()
    
    # Phase 9: Pre-Contact Call-to-Action Card & Floating Hire Me Button
    render_hire_me()
    
    # Phase 6: Contact Section & Form
    render_contact()


if __name__ == "__main__":
    main()
