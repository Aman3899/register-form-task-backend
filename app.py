from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- NEW
import pandas as pd
import os

app = Flask(__name__)
CORS(app)  # <-- NEW: allow your frontend to access API

CSV_FILE = "/home/amanullah1/mysite/submissions.csv"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data received"}), 400

    new_entry = pd.DataFrame([data])

    if os.path.exists(CSV_FILE):
        existing = pd.read_csv(CSV_FILE)
        new_entry = pd.concat([existing, new_entry], ignore_index=True)

    new_entry.to_csv(CSV_FILE, index=False)

    return jsonify({"status": "success", "message": "Data saved"})
