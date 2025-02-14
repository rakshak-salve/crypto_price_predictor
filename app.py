from flask import Flask, render_template, jsonify
from flask_cors import CORS
import pickle
import numpy as np
from datetime import datetime
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load trained models
try:
    with open("crypto_model.pkl", "rb") as model_file:
        models = pickle.load(model_file)
    btc_model = models.get("btc_model", None)
    eth_model = models.get("eth_model", None)
except Exception as e:
    btc_model, eth_model = None, None
    print(f"❌ Error loading models: {e}")


# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Predict route
@app.route("/predict", methods=["GET"])
def predict_price():
    if btc_model is None or eth_model is None:
        return jsonify({"error": "Models not loaded correctly"}), 500
    try:
        # Get current timestamp and predict prices
        current_timestamp = int(datetime.now().timestamp())
        latest_timestamp = np.array([[current_timestamp]])
        
        btc_pred = btc_model.predict(latest_timestamp)[0]
        eth_pred = eth_model.predict(latest_timestamp)[0]

        # Prepare response
        response = {
            "Bitcoin": {"Predicted Price": float(btc_pred)},
            "Ethereum": {"Predicted Price": float(eth_pred)},
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT if set, otherwise default to 5000
    app.run(host="0.0.0.0", port=port)  # Bind to 0.0.0.0
