import os
import streamlit as st
import streamlit.components.v1 as components

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def get_ga_measurement_id() -> str:
    """
    Retrieves Google Analytics 4 Measurement ID from environment, Streamlit secrets,
    or defaults to 'G-9HZN7HG1DN'.
    """
    ga_id = os.getenv("GA_MEASUREMENT_ID", "").strip()
    if not ga_id:
        try:
            if hasattr(st, "secrets") and "GA_MEASUREMENT_ID" in st.secrets:
                ga_id = str(st.secrets["GA_MEASUREMENT_ID"]).strip()
        except Exception:
            pass
    if not ga_id:
        ga_id = "G-9HZN7HG1DN"
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
    Uses Streamlit iframe component to execute JavaScript and mount the GA script
    directly to window.parent.document.head for reliable detection and tracking.
    """
    ga_id = get_ga_measurement_id()
    if not ga_id or ga_id == "G-XXXXXXXXXX":
        return

    ga_html = f"""
    <script>
    (function() {{
      var gaId = "{ga_id}";
      if (!gaId || gaId === "G-XXXXXXXXXX") return;

      var targetDoc = document;
      var targetWin = window;
      try {{
        if (window.parent && window.parent.document) {{
          targetDoc = window.parent.document;
          targetWin = window.parent;
        }}
      }} catch (e) {{
        // Fallback to iframe context if cross-origin
      }}

      // 1. Inject gtag.js script tag into main page document head
      if (!targetDoc.getElementById("ga-gtag-script")) {{
        var script = targetDoc.createElement("script");
        script.id = "ga-gtag-script";
        script.async = true;
        script.src = "https://www.googletagmanager.com/gtag/js?id=" + gaId;
        targetDoc.head.appendChild(script);
      }}

      // 2. Initialize dataLayer & gtag function on target window
      targetWin.dataLayer = targetWin.dataLayer || [];
      function gtag() {{
        targetWin.dataLayer.push(arguments);
      }}
      targetWin.gtag = gtag;

      gtag("js", new Date());
      gtag("config", gaId, {{
        "page_title": targetDoc.title || "Bhaskar Mandal | Portfolio",
        "page_location": targetWin.location.href,
        "send_page_view": true
      }});

      // Sync window.dataLayer for iframe context
      if (targetWin !== window) {{
        window.dataLayer = targetWin.dataLayer;
        window.gtag = gtag;
      }}

      // 3. Auto-attach click listeners for GA4 custom event tracking
      function setupTracking() {{
        if (targetDoc._ga4TrackingAttached) return;
        targetDoc._ga4TrackingAttached = true;

        targetDoc.body.addEventListener("click", function(e) {{
          var target = e.target.closest("a, button");
          if (!target) return;

          var href = target.getAttribute("href") || "";
          var text = (target.innerText || "").trim();

          // 1. Resume Downloads
          if (href.includes("pdf") || target.classList.contains("download-resume-btn") || text.toLowerCase().includes("resume")) {{
            gtag("event", "resume_download", {{
              "event_category": "Engagement",
              "event_label": "Download Resume"
            }});
          }}

          // 2. GitHub Clicks
          if (href.includes("github.com")) {{
            gtag("event", "github_click", {{
              "event_category": "Outbound",
              "event_label": href
            }});
          }}

          // 3. LinkedIn Clicks
          if (href.includes("linkedin.com")) {{
            gtag("event", "linkedin_click", {{
              "event_category": "Outbound",
              "event_label": href
            }});
          }}

          // 4. Project Button Clicks
          if (target.classList.contains("project-btn-github") || target.classList.contains("project-btn-demo") || href.includes("streamlit.app") || href.includes("hf.space")) {{
            gtag("event", "project_click", {{
              "event_category": "Projects",
              "event_label": text + " | " + href
            }});
          }}
        }}, true);
      }}

      if (targetDoc.readyState === "complete" || targetDoc.readyState === "interactive") {{
        setupTracking();
      }} else {{
        targetDoc.addEventListener("DOMContentLoaded", setupTracking);
      }}
    }})();
    </script>
    """
    components.html(ga_html, height=0, width=0)

