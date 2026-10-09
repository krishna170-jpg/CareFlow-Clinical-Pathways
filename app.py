from pathlib import Path
import random, smtplib, ssl, re
from email.message import EmailMessage
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CareFlow: Clinical Pathway Process Mining", page_icon="✚", layout="wide")

# Configure these in Streamlit Cloud -> App -> Settings -> Secrets.
def send_otp(to_email: str, otp: str) -> None:
    cfg = st.secrets.get("smtp", {})
    host = cfg.get("host", "smtp.gmail.com")
    port = int(cfg.get("port", 465))
    username = cfg.get("username", "")
    password = cfg.get("password", "")
    sender = cfg.get("sender", username)
    if not username or not password or not sender:
        raise RuntimeError("Email delivery is not configured yet. Add SMTP settings in Streamlit Cloud Secrets; see README.md.")
    msg = EmailMessage()
    msg["Subject"] = "Your CareFlow signup verification code"
    msg["From"] = sender
    msg["To"] = to_email
    msg.set_content(f"Your CareFlow verification code is {otp}. It expires in 10 minutes. If you did not request this, ignore this email.")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context, timeout=20) as server:
        server.login(username, password)
        server.send_message(msg)

if "otp_verified" not in st.session_state:
    st.session_state.otp_verified = False
if "otp_code" not in st.session_state:
    st.session_state.otp_code = None
if "otp_email" not in st.session_state:
    st.session_state.otp_email = ""
if "otp_expiry" not in st.session_state:
    st.session_state.otp_expiry = 0
if "otp_attempts" not in st.session_state:
    st.session_state.otp_attempts = 0

if not st.session_state.otp_verified:
    st.markdown("<div style='text-align:center;font-size:38px;font-weight:800;color:#087f8c'>✚ CareFlow</div><div style='text-align:center;color:gray'>CLINICAL PATHWAY INTELLIGENCE</div>", unsafe_allow_html=True)
    st.title("Create your CareFlow account")
    st.write("Enter your email address and verify it with a one-time code sent to your inbox.")
    with st.form("signup_form"):
        email = st.text_input("Email address", value=st.session_state.otp_email, placeholder="you@example.com").strip().lower()
        name = st.text_input("Full name")
        role = st.selectbox("Role", ["Care coordinator", "Clinician", "Nurse", "Department manager", "Quality & governance", "Administrator", "Student / Demo user"])
        sent = st.form_submit_button("Send email OTP", use_container_width=True)
    if sent:
        if "@" not in email or "." not in email.split("@")[-1]:
            st.error("Enter a valid email address.")
        else:
            otp = f"{random.SystemRandom().randint(0, 999999):06d}"
            try:
                send_otp(email, otp)
                import time
                st.session_state.otp_code = otp
                st.session_state.otp_email = email
                st.session_state.otp_name = name.strip()
                st.session_state.otp_role = role
                st.session_state.otp_expiry = time.time() + 600
                st.session_state.otp_attempts = 0
                st.success("Verification code sent. Check your inbox and spam folder.")
            except Exception as exc:
                st.error(str(exc))
    if st.session_state.otp_code:
        st.divider()
        st.caption(f"OTP sent to {st.session_state.otp_email}. Code expires in 10 minutes.")
        with st.form("verify_otp_form"):
            entered = st.text_input("6-digit email OTP", max_chars=6, placeholder="123456")
            verified = st.form_submit_button("Verify email and continue", use_container_width=True)
        if verified:
            import time
            st.session_state.otp_attempts += 1
            if time.time() > st.session_state.otp_expiry:
                st.session_state.otp_code = None
                st.error("Code expired. Send a new OTP.")
            elif st.session_state.otp_attempts > 5:
                st.session_state.otp_code = None
                st.error("Too many attempts. Request a new OTP.")
            elif entered.strip() == st.session_state.otp_code:
                st.session_state.otp_verified = True
                st.session_state.otp_code = None
                st.success("Email verified. Opening CareFlow…")
                st.rerun()
            else:
                st.error("Incorrect OTP. Please try again.")
    st.info("This demo verifies email ownership. For production use, add persistent account storage and a secure authentication provider. No real patient data should be entered.")
    st.stop()

html_path = Path(__file__).parent / "index.html"
if not html_path.exists():
    st.error("index.html is missing. Upload it beside app.py in your GitHub repository.")
    st.stop()
html = html_path.read_text(encoding="utf-8")
# Remove the old browser-only login/signup overlay; Streamlit OTP verification gates access now.
html = re.sub(r'<div id="cf-login".*?</div>\s*</div>\s*</div>', '', html, count=1, flags=re.S)
html = re.sub(r'<script>\s*\(function\(\)\{const overlay=document\.getElementById\([\'\"]cf-login[\'\"]\).*?</script>', '', html, count=1, flags=re.S)
st.markdown("<style>[data-testid='stHeader'], footer {visibility:hidden} .block-container {padding:0;max-width:100%}</style>", unsafe_allow_html=True)
with st.sidebar:
    st.success("Email verified")
    st.write(st.session_state.otp_email)
    if st.button("Sign out"):
        st.session_state.otp_verified = False
        st.rerun()
components.html(html, height=1800, scrolling=True)
