from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  # Allow frontend JS to make requests

# Load the trained model
model = joblib.load("liver_disease_model.pkl")

@app.route("/")
def home():
    return "Liver Disease Predictor API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    try:
        features = [
            float(data['Total_Bilirubin']),
            float(data['Direct_Bilirubin']),
            float(data['Alkaline_Phosphotase']),
            float(data['Alamine_Aminotransferase']),
            float(data['Total_Proteins']),
            float(data['Albumin']),
            float(data['Albumin_and_Globulin_Ratio'])
        ]

        prediction = model.predict([features])[0]
        probability = model.predict_proba([features])[0][1]

        return jsonify({
            "prediction": int(prediction),
            "probability": round(probability * 100, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = [[
        data['Total_Bilirubin'], data['Direct_Bilirubin'],
        data['Alkaline_Phosphotase'], data['Alamine_Aminotransferase'],
        data['Total_Proteins'], data['Albumin'], data['Albumin_and_Globulin_Ratio']
    ]]
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][int(prediction)] * 100
    label = "LIVER DISEASE" if prediction == 1 else "NO DISEASE"
    return jsonify({
        "prediction": label,
        "probability": round(probability, 2),
        "risk_class": "risk-high" if prediction == 1 else "risk-low"
    })

