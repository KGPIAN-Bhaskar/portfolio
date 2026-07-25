import os
import streamlit as st
from utils.html_render import render_html

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def get_ga_measurement_id() -> str:
    """
    Retrieves Google Analytics 4 Measurement ID from environment or Streamlit secrets.
    """
    ga_id = os.getenv("GA_MEASUREMENT_ID", "").strip()
    if not ga_id and hasattr(st, "secrets") and "GA_MEASUREMENT_ID" in st.secrets:
        ga_id = st.secrets["GA_MEASUREMENT_ID"].strip()
    return ga_id


def inject_ga4():
    """
    Silently injects Google Analytics 4 tracking code and event listeners for:
    - Page views
    - Resume downloads
    - Contact form submissions
    - GitHub clicks
    - LinkedIn clicks
    - Project button clicks
    """
    ga_id = get_ga_measurement_id()
    if not ga_id:
        ga_id = "G-XXXXXXXXXX"

    ga_html = f"""
    <!-- Google Analytics 4 Tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={ga_id}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());

      gtag('config', '{ga_id}', {{
        'page_title': document.title,
        'page_location': window.location.href
      }});

      // Auto-attach click listeners for GA4 custom event tracking
      document.addEventListener('DOMContentLoaded', function() {{
        document.body.addEventListener('click', function(e) {{
          var target = e.target.closest('a, button');
          if (!target) return;

          var href = target.getAttribute('href') || '';
          var text = (target.innerText || '').trim();

          // 1. Resume Downloads
          if (href.includes('resume.pdf') || target.classList.contains('download-resume-btn')) {{
            gtag('event', 'resume_download', {{
              'event_category': 'Engagement',
              'event_label': 'Download Resume'
            }});
          }}

          // 2. GitHub Clicks
          if (href.includes('github.com')) {{
            gtag('event', 'github_click', {{
              'event_category': 'Outbound',
              'event_label': href
            }});
          }}

          // 3. LinkedIn Clicks
          if (href.includes('linkedin.com')) {{
            gtag('event', 'linkedin_click', {{
              'event_category': 'Outbound',
              'event_label': href
            }});
          }}

          // 4. Project Button Clicks
          if (target.classList.contains('project-btn-github') || target.classList.contains('project-btn-demo')) {{
            gtag('event', 'project_click', {{
              'event_category': 'Projects',
              'event_label': text + ' | ' + href
            }});
          }}
        }}, true);
      }});
    </script>
    """
    render_html(ga_html)
