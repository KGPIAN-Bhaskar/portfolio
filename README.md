# Bhaskar Mandal - GenAI Engineer & Data Scientist Portfolio

A modern, high-aesthetic dark glassmorphism interactive portfolio web application built with **Streamlit**, **Python**, **CSS3**, and **Google Apps Script / GA4 Telemetry**.

---

## 🌟 Key Features

- **⚡ Dark Glassmorphic Design System**: Modern translucent card components with neon emerald accents and custom CSS transitions.
- **🚀 Project Showcases**: Interactive project grid with live Streamlit demo links and GitHub code repositories.
- **📚 Curated Interview Kits**: Streamlit native modal dialog image previews and direct PDF downloads for GenAI, ML, and Data Science kits.
- **📬 Automated Contact Pipeline**: Contact form integrated directly with Google Apps Script Web App for auto-appending submissions to Google Sheets and sending instant email notifications.
- **📈 Google Analytics 4 (GA4) Telemetry**: Parent window iframe script mounting for reliable visitor pageview and click event tracking.
- **⚡ Production Optimization & Caching**: Centralized binary asset and JSON caching using `@st.cache_data` to eliminate disk I/O on page reruns.

---

## 📁 Directory Architecture

```
Portfolio/
├── .streamlit/
│   └── config.toml           # Streamlit theme & server configuration
├── assets/
│   ├── profile.png           # Profile photo asset
│   └── projects/             # High-resolution project banners
├── components/
│   ├── about.py              # About Me section component
│   ├── contact.py            # Contact section & form component
│   ├── experience.py         # Work experience timeline component
│   ├── hero.py               # Home / Hero section component
│   ├── hire_me.py            # Floating CTA & Hire Me card component
│   ├── interview_kits.py     # Interview kits section & modal dialogs
│   ├── navbar.py             # Fixed top glassmorphism navbar
│   ├── projects.py           # Featured projects grid component
│   ├── section.py            # Reusable section layout wrapper
│   └── skills.py             # Technical skills progress bars component
├── data/
│   ├── experience.json       # Work experience timeline dataset
│   ├── interview_kits.json   # Interview kits metadata dataset
│   ├── profile_data.py       # Core profile metadata
│   ├── projects.json         # Featured projects dataset
│   └── skills.json           # Technical skills categories dataset
├── styles/
│   └── main.css              # Glassmorphism design system & micro-animations
├── utils/
│   ├── analytics.py          # Google Analytics 4 iframe script mounting
│   ├── asset_loader.py       # Centralized @st.cache_data file loader
│   ├── css_loader.py         # Custom CSS injection utility
│   ├── google_sheets.py      # Google Apps Script Web App contact API
│   └── html_render.py        # Safe HTML rendering utility
├── app.py                    # Main Streamlit application entry point
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 🛠️ Environment Variables & Secrets Setup

Create a `.env` file in the root directory (or configure Secrets in Streamlit Cloud):

```env
# Google Apps Script Deployment URL for Contact Form
GOOGLE_APPS_SCRIPT_URL=https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec

# Google Analytics 4 Measurement ID
GA_MEASUREMENT_ID=G-XXXXXXXXXX
```

---

## 💻 Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KGPIAN-Bhaskar/portfolio.git
   cd portfolio
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run locally**:
   ```bash
   streamlit run app.py
   ```

---

## 🔒 Security & Performance Features

- **Input Sanitization**: HTML escaping on all contact form inputs (`name`, `email`, `subject`, `message`) to prevent XSS payloads.
- **Resource Caching**: Image files, PDFs, and JSON datasets cached using `@st.cache_data` with automatic `mtime` cache invalidation.
- **GPU Acceleration**: Smooth CSS transitions offloaded to browser compositor layers via `translate3d` and `will-change`.
