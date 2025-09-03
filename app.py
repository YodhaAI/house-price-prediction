from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load model and features
model = joblib.load("rf_tuned_model.pkl")
features = joblib.load("model_features.pkl")

# Home route - renders the HTML form
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form inputs
        data = {
            "OverallQual": int(request.form["OverallQual"]),
            "GrLivArea": float(request.form["GrLivArea"]),
            "TotalBsmtSF": float(request.form["TotalBsmtSF"]),
            "2ndFlrSF": float(request.form["2ndFlrSF"]),
            "1stFlrSF": float(request.form["1stFlrSF"]),
            "GarageArea": float(request.form["GarageArea"]),
            "YearBuilt": int(request.form["YearBuilt"]),
            "FullBath": int(request.form["FullBath"]),
            "LotArea": float(request.form["LotArea"]),
            "GarageCars": int(request.form["GarageCars"])
        }

        # Convert into DataFrame
        input_df = pd.DataFrame([data])
        input_df = input_df.reindex(columns=features, fill_value=0)  # match training features

        # Prediction
        pred_log = model.predict(input_df)[0]
        pred = np.expm1(pred_log)

        # 🟢 Pass prediction_text and pred separately
        return render_template(
            "index.html",
            prediction_text=f"Predicted House Price: ${pred:,.2f}",
            pred=round(pred, 2)   # send numeric value for chart
        )

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
