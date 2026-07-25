import re
import streamlit as st
from data.profile_data import PROFILE_DATA
from utils.html_render import render_html
from utils.google_sheets import send_to_google_sheets

def is_valid_email(email: str) -> bool:
    """
    Validates email format using regex.
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email.strip()))


def render_contact():
    """
    Renders the Contact section featuring contact metadata callout and a Google Sheets + Email connected form.
    """
    # SVG Icons
    email_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>"""
    phone_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>"""
    map_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"></path><circle cx="12" cy="10" r="3"></circle></svg>"""
    github_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"></path><path d="M9 18c-4.51 2-5-2-7-2"></path></svg>"""
    linkedin_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>"""

    # Anchored Section Title Header
    header_html = """
    <div id="contact" style="position: relative; top: -60px;"></div>
    <div class="about-header-container">
        <h2 class="about-main-title">GET IN <span class="about-title-highlight">TOUCH</span></h2>
        <div class="about-title-underline"></div>
    </div>
    """
    render_html(header_html)

    # Open Glass Card Container
    st.markdown('<div class="contact-card-container">', unsafe_allow_html=True)
    
    col_info, col_form = st.columns([1, 1.3], gap="large")
    
    with col_info:
        info_html = f"""
        <div class="contact-info-side">
            <div>
                <h3 class="contact-info-title">Let's Connect & Collaborate</h3>
                <p class="contact-info-desc">
                    Interested in Generative AI development, RAG systems, or Multi-Agent applications? Feel free to reach out for opportunities, research collaborations, or technical inquiries.
                </p>
                
                <div class="contact-details-list">
                    <div class="contact-detail-item">
                        <div class="contact-icon-wrapper">{email_svg}</div>
                        <div class="contact-detail-text">
                            <span class="contact-detail-label">Email Address</span>
                            <a href="{PROFILE_DATA['social']['email']}" class="contact-detail-value">{PROFILE_DATA['email']}</a>
                        </div>
                    </div>
                    
                    <div class="contact-detail-item">
                        <div class="contact-icon-wrapper">{phone_svg}</div>
                        <div class="contact-detail-text">
                            <span class="contact-detail-label">Phone Number</span>
                            <span class="contact-detail-value">{PROFILE_DATA['phone']}</span>
                        </div>
                    </div>
                    
                    <div class="contact-detail-item">
                        <div class="contact-icon-wrapper">{map_svg}</div>
                        <div class="contact-detail-text">
                            <span class="contact-detail-label">Location</span>
                            <span class="contact-detail-value">IIT Kharagpur, West Bengal, India</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <div>
                <div style="font-size: 0.85rem; color: #94a3b8; font-family: 'Fira Code', monospace; margin-bottom: 0.75rem;">
                    SOCIAL NETWORKS
                </div>
                <div class="hero-social-container" style="justify-content: flex-start;">
                    <a href="{PROFILE_DATA['social']['github']}" target="_blank" rel="noopener noreferrer" class="social-icon-btn" title="GitHub">
                        {github_svg}
                    </a>
                    <a href="{PROFILE_DATA['social']['linkedin']}" target="_blank" rel="noopener noreferrer" class="social-icon-btn" title="LinkedIn">
                        {linkedin_svg}
                    </a>
                </div>
            </div>
        </div>
        """
        render_html(info_html)

    with col_form:
        with st.form(key="contact_form", clear_on_submit=True):
            st.markdown('<h3 style="font-size: 1.4rem; font-weight: 700; color: #ffffff; margin-bottom: 1rem;">Send a Message</h3>', unsafe_allow_html=True)
            
            name = st.text_input("Name *", placeholder="Enter your full name")
            email = st.text_input("Email *", placeholder="enter.your.email@domain.com")
            subject = st.text_input("Subject *", placeholder="Topic or project inquiry")
            message = st.text_area("Message *", placeholder="Type your detailed message here...", height=130)
            
            submit_btn = st.form_submit_button(label="🚀 Send Message")
            
            if submit_btn:
                if not name.strip() or not email.strip() or not subject.strip() or not message.strip():
                    st.warning("⚠️ Please fill out all required fields before submitting.")
                elif not is_valid_email(email):
                    st.error("❌ Please enter a valid email address (e.g. name@domain.com).")
                else:
                    with st.spinner("Saving message & sending email notification..."):
                        success, feedback_msg = send_to_google_sheets(name, email, subject, message)
                        if success:
                            st.success(f"✅ {feedback_msg}")
                        else:
                            st.error(f"❌ {feedback_msg}")

    st.markdown('</div>', unsafe_allow_html=True)
