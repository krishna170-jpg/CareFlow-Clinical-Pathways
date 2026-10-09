# CareFlow — Clinical Pathway Process Mining Demo

A fictional hospital-operations dashboard demo with sections for Departments, Task Board, Reports, Patient Flow, Clinical Pathways, Care Teams, and Governance.

## Run locally with Python

1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   python app.py
   ```

5. Open <http://127.0.0.1:5000> in your browser.

The demo API endpoints are `/api/health` and `/api/departments`.

## GitHub Pages note

GitHub Pages serves static HTML/CSS/JavaScript only; it does **not** run Python or Flask. The existing `index.html` can still be published on GitHub Pages, but `app.py` must run on a Python-capable host to provide backend/API functionality.

## Demo data and safety

All names, counts, and metrics are fictional examples for demonstration. This is not a production clinical system. Do not use real patient data. A real deployment would require authentication, authorization, secure storage, audit logging, validation, and appropriate clinical/security review.
