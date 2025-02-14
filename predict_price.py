import pickle
import numpy as np
from datetime import datetime

# Load the trained model
with open("crypto_model.pkl", "rb") as model_file:
    models = pickle.load(model_file)

btc_model = models["btc_model"]
eth_model = models["eth_model"]

# Predict future prices
def predict_future_price():
    current_timestamp = int(datetime.now().timestamp())
    latest_timestamp = np.array([[current_timestamp]])

    predicted_btc_price = btc_model.predict(latest_timestamp)[0]
    predicted_eth_price = eth_model.predict(latest_timestamp)[0]

    print(f"🔮 Predicted Bitcoin Price: ${predicted_btc_price:.2f}")
    print(f"🔮 Predicted Ethereum Price: ${predicted_eth_price:.2f}")

predict_future_price()
