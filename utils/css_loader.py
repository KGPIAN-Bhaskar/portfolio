import os
import streamlit as st

def load_css(file_path: str = "styles/main.css") -> bool:
    """
    Safely loads and injects custom CSS styling into the Streamlit app.
    
    Args:
        file_path (str): Relative or absolute path to the CSS file.
        
    Returns:
        bool: True if loaded successfully, False otherwise.
    """
    try:
        # Resolve path relative to working directory or project base
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        target_path = os.path.join(base_dir, file_path) if not os.path.isabs(file_path) else file_path
        
        if os.path.exists(target_path):
            with open(target_path, "r", encoding="utf-8") as f:
                css_content = f.read()
            st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
            return True
        else:
            st.warning(f"CSS file not found at: {target_path}")
            return False
    except Exception as e:
        st.error(f"Error loading CSS file '{file_path}': {str(e)}")
        return False
