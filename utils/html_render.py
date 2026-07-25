import re
import streamlit as st

def render_html(html_str: str) -> None:
    """
    Renders raw HTML safely in Streamlit without allowing Markdown-IT to break it into raw code blocks.
    1. Removes all HTML comments (<!-- ... -->) which break Markdown-IT block parsing.
    2. Strips leading/trailing whitespace from each line and joins into a single contiguous string.
    """
    # Remove all HTML comments
    html_no_comments = re.sub(r'<!--.*?-->', '', html_str, flags=re.DOTALL)
    
    # Clean and minify into a single contiguous HTML string
    clean_html = "".join([line.strip() for line in html_no_comments.splitlines() if line.strip()])
    
    # Render in Streamlit
    st.markdown(clean_html, unsafe_allow_html=True)
