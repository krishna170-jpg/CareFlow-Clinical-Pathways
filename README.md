# CareFlow — Clinical Pathway Process Mining

CareFlow is a fictional, interactive dashboard demo for department performance, task coordination, reports, patient flow, clinical pathways, care teams, and governance.

## Deploy on Streamlit Community Cloud

1. Put `app.py`, `index.html`, and `requirements.txt` together in the **root** of your GitHub repository.
2. Open https://share.streamlit.io/ and sign in with GitHub.
3. Choose **Create app** → **Yup, I have an app**.
4. Select your repository, branch `main`, and main file path `app.py`.
5. Click **Deploy** and wait for the build to finish.

Streamlit Cloud runs `app.py`; the script embeds `index.html` as an interactive dashboard. Do not use the previous Flask `app.run(...)` line for Streamlit Cloud.

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Data and safety

All names, counts, pathways, and operational metrics are synthetic demo data. This project is not a real clinical information system. Do not upload real patient or other sensitive health information.
