# MetraCheck Prototype

Frontend: HTML + CSS + JavaScript
Backend: Python + Flask

## Run

1. Open a terminal in `backend`.
2. Create/activate a virtual environment (recommended).
3. Install:
   pip install -r requirements.txt
4. Start backend:
   python app.py
5. Open `frontend/index.html` in your browser.

The frontend calls `http://127.0.0.1:5000`.

## Prototype scope

The backend accepts an uploaded package image, stores it in `backend/uploads/`, creates a prototype compliance result, and stores the inspection in memory.

The supplied problem statement calls for image scanning, declaration extraction, validation, readability/font-size analysis, violation detection, reports, history, role-based access and dashboards. This prototype provides the UI/workflow and an API seam for adding real OCR, computer vision and a formal Legal Metrology rule engine.

Do not treat the prototype's randomized analysis as a legal compliance determination.
