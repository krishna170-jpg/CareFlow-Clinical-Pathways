# CareFlow — Clinical Pathway Process Mining

CareFlow is an interactive dashboard demo with fictional sample data for Departments, Task Board, Reports, Patient Flow, Clinical Pathways, Care Teams, and Governance.

## Deploy on Streamlit Community Cloud
1. Upload `app.py`, `index.html`, and `requirements.txt` to the root of your GitHub repository.
2. Visit https://share.streamlit.io/ and sign in with GitHub.
3. Choose Create app and select your repository, branch `main`, and main file path `app.py`.
4. Tap Deploy and wait for the build to finish.

## Run locally
```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Demo-data notice
All names, counts, journey IDs, and metrics are fictional demonstration data. This is not a real clinical information system. Never upload real patient information.
