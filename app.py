from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CareFlow: Clinical Pathway Process Mining", page_icon="✚", layout="wide")
html_path = Path(__file__).parent / "index.html"
if not html_path.exists():
    st.error("index.html is missing. Upload it beside app.py in your GitHub repository.")
    st.stop()
html = html_path.read_text(encoding="utf-8")
st.markdown("""<style>[data-testid='stHeader'], footer {visibility:hidden} .block-container {padding:0;max-width:100%}</style>""", unsafe_allow_html=True)
components.html(html, height=1600, scrolling=True)
