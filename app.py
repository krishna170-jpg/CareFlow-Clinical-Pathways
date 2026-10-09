"""CareFlow demo web app.

Run locally:
    python -m pip install -r requirements.txt
    python app.py
Then open http://127.0.0.1:5000

All records shown by this demo are fictional. Do not use real patient data.
"""
from flask import Flask, jsonify, send_from_directory
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, static_folder=None)

DEPARTMENTS = [
    {"name": "Emergency", "lead": "Dr. Maya Chen", "active_cases": 42, "capacity_pct": 91, "status": "At risk"},
    {"name": "Cardiology", "lead": "Dr. Arjun Patel", "active_cases": 31, "capacity_pct": 78, "status": "On track"},
    {"name": "Neurology", "lead": "Dr. Leena Rao", "active_cases": 24, "capacity_pct": 83, "status": "Monitor"},
    {"name": "General Medicine", "lead": "Dr. Omar Khan", "active_cases": 56, "capacity_pct": 74, "status": "On track"},
    {"name": "Orthopedics", "lead": "Dr. Sofia Martin", "active_cases": 28, "capacity_pct": 88, "status": "Monitor"},
    {"name": "Oncology", "lead": "Dr. Ethan Cole", "active_cases": 19, "capacity_pct": 68, "status": "On track"},
    {"name": "ICU", "lead": "Dr. Noah Williams", "active_cases": 15, "capacity_pct": 94, "status": "Monitor"},
]

@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "app": "CareFlow demo", "demo_data": True})

@app.get("/api/departments")
def departments():
    return jsonify(DEPARTMENTS)

@app.get("/robots.txt")
def robots():
    return send_from_directory(BASE_DIR, "robots.txt")

@app.get("/sitemap.xml")
def sitemap():
    return send_from_directory(BASE_DIR, "sitemap.xml")

if __name__ == "__main__":
    # Local development server only; use a production WSGI server for deployment.
    app.run(host="127.0.0.1", port=5000, debug=True)
