"""CareFlow: Clinical Pathway Process Mining — Streamlit Cloud entrypoint.

All dashboard records are synthetic demo data. Never use real patient information.
Deploy with: streamlit run app.py
"""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

BASE_DIR = Path(__file__).resolve().parent
HTML_FILE = BASE_DIR / "index.html"

st.set_page_config(
    page_title="CareFlow | Clinical Pathway Process Mining",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep Streamlit's outer frame clean so the existing interactive dashboard
# can render inside an iframe. The dashboard's own JavaScript handles tabs,
# task forms, filters, and CSV exports.
st.markdown(
    """
    <style>
      .block-container {padding-top: .6rem; padding-bottom: .5rem; max-width: 100%;}
      header[data-testid="stHeader"] {height: 0rem;}
      footer {visibility: hidden;}
      div[data-testid="stToolbar"] {visibility: hidden; height: 0%; position: fixed;}
    </style>
    """,
    unsafe_allow_html=True,
)

if not HTML_FILE.exists():
    st.error("CareFlow dashboard file is missing. Ensure index.html is in the repository root beside app.py.")
    st.stop()

html = HTML_FILE.read_text(encoding="utf-8")
components.html(html, height=1800, scrolling=True)

with st.expander("About this demo and troubleshooting"):
    st.write(
        "CareFlow is a demonstration dashboard populated with fictional department, "
        "care-team, task, pathway, and patient-flow records. It is not a clinical system "
        "and must not be used for clinical decisions."
    )
    st.caption("If the dashboard does not update after a code change, use Streamlit's menu and select Rerun, or reboot the app from Manage app.")
