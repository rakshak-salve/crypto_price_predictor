from flask import Flask, render_template, jsonify
import pickle
import numpy as np
from datetime import datetime

# Load trained models
with open("crypto_model.pkl", "rb") as model_file:
    models = pickle.load(model_file)

btc_model = models["btc_model"]
eth_model = models["eth_model"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET"])
def predict_price():
    current_timestamp = int(datetime.now().timestamp())
    latest_timestamp = np.array([[current_timestamp]])

    btc_pred = btc_model.predict(latest_timestamp)[0]
    eth_pred = eth_model.predict(latest_timestamp)[0]

    response = {
        "Bitcoin": {"Predicted Price": float(btc_pred)},
        "Ethereum": {"Predicted Price": float(eth_pred)},
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
