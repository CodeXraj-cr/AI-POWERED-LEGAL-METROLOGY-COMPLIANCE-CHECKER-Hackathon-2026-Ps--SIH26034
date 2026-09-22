from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from pathlib import Path
import random

app = Flask(__name__)
CORS(app)

UPLOADS = Path("uploads")
UPLOADS.mkdir(exist_ok=True)

# Prototype in-memory repository.
INSPECTIONS = [
    {"date":"22 Sep 2026","product":"Packaged Food — 500 g","detected":9,"total":9,"status":"Compliant","readability":"Good"},
    {"date":"22 Sep 2026","product":"Household Cleaner — 1 L","detected":7,"total":9,"status":"Review","readability":"Good"},
    {"date":"21 Sep 2026","product":"Personal Care — 200 ml","detected":6,"total":9,"status":"Non-compliant","readability":"Low"},
]

@app.get("/api/health")
def health():
    return jsonify({"status":"ok","service":"MetraCheck prototype backend"})

@app.get("/api/inspections")
def inspections():
    return jsonify(INSPECTIONS)

@app.post("/api/scan")
def scan():
    image = request.files.get("image")
    if not image:
        return jsonify({"error":"No image uploaded"}), 400

    safe_name = image.filename.replace("/", "_").replace("\\", "_")
    image.save(UPLOADS / safe_name)

    # Prototype analysis:
    # A production version can plug OCR + image detection + the official rule engine here.
    detected = random.choice([7, 8, 9])
    total = 9
    score = round(detected / total * 100)
    status = "Compliant" if detected == total else ("Review" if detected >= 7 else "Non-compliant")

    record = {
        "date": datetime.now().strftime("%d %b %Y"),
        "product": safe_name,
        "detected": detected,
        "total": total,
        "status": status,
        "readability": "Good" if detected >= 8 else "Review",
    }
    INSPECTIONS.append(record)

    return jsonify({
        **record,
        "score": score,
        "message": "Prototype rule analysis completed. OCR, font-size measurement and detailed legal-rule validation should be connected for production use."
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
