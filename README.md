# CareFlow: Clinical Pathway Process Mining

Streamlit-hosted interactive dashboard with fictional demonstration data for Patient Flow, Clinical Pathways, Care Teams and Governance. Signup verifies email by sending a one-time password (OTP) through SMTP.

## Deploy on Streamlit Community Cloud
1. Upload `app.py`, `index.html`, and `requirements.txt` to the root of your GitHub repository.
2. On https://share.streamlit.io choose the repository, branch `main`, and main file `app.py`.
3. In Streamlit Cloud, open **App settings → Secrets** and add SMTP settings (example below). Use an email provider you control.
4. Save secrets and reboot/redeploy the app.

## SMTP configuration example (Gmail)
Create a Google App Password for a Google account with 2-Step Verification enabled. Do not use your normal Google password. Keep this secret private and never commit it to GitHub.

```toml
[smtp]
host = "smtp.gmail.com"
port = 465
username = "your-sender@gmail.com"
password = "your-16-character-app-password"
sender = "your-sender@gmail.com"
```

The email OTP expires after 10 minutes and has a maximum of five verification attempts per issued code. If SMTP secrets are missing, email sending will fail with a setup message.

## Important security notes
- OTP email delivery requires valid SMTP credentials; this ZIP cannot send mail until you configure them.
- This is a demo sign-up flow, not a complete production identity system. It does not create a persistent account database; verification is held in the Streamlit session.
- Use a production identity provider and persistent user store before using real accounts. Never enter real patient data. All dashboard records are fictional demo data.
