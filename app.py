from flask import Flask, render_template, request, jsonify
from pathlib import Path
import pandas as pd
import joblib

ROOT = Path(__file__).parent
app = Flask(__name__)
model = joblib.load(ROOT / "house_price_model.joblib")

LOCATIONS = [
    "Hyderabad - Gachibowli", "Hyderabad - Kondapur", "Hyderabad - Kukatpally",
    "Hyderabad - Miyapur", "Hyderabad - Uppal", "Bengaluru - Whitefield",
    "Bengaluru - Electronic City", "Chennai - OMR", "Pune - Hinjewadi", "Mumbai - Thane"
]

@app.get("/")
def home():
    return render_template("index.html", locations=LOCATIONS)

@app.post("/predict")
def predict():
    try:
        payload = request.get_json(force=True)
        row = pd.DataFrame([{
            "location": payload["location"],
            "area_sqft": int(payload["area_sqft"]),
            "bhk": int(payload["bhk"]),
            "bathrooms": int(payload["bathrooms"]),
            "property_age_years": int(payload["property_age_years"]),
            "floor": int(payload["floor"]),
            "parking": int(payload["parking"])
        }])
        if row["area_sqft"].iloc[0] < 300 or row["area_sqft"].iloc[0] > 10000:
            return jsonify({"error": "Area must be between 300 and 10,000 sq. ft."}), 400
        estimate = float(model.predict(row)[0])
        return jsonify({
            "price_lakhs": round(estimate, 2),
            "price_crore": round(estimate / 100, 2),
            "formatted": f"₹{estimate:,.2f} lakh"
        })
    except (KeyError, ValueError, TypeError):
        return jsonify({"error": "Please check all property details and try again."}), 400

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
