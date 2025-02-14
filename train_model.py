# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import pickle

# Step 1: Load the dataset
file_path = "crypto_prices.csv"
data = pd.read_csv(file_path)

# Step 2: Prepare the data for training
data["Timestamp"] = pd.to_datetime(data["Timestamp"])
data["Timestamp"] = data["Timestamp"].astype('int64') // 10**9  # Convert to UNIX timestamp

# Define input (X) and output (Y) for the model
X = data["Timestamp"].values.reshape(-1, 1)
Y_btc = data["Bitcoin Price (USD)"].values
Y_eth = data["Ethereum Price (USD)"].values

# Step 3: Split data into training & testing
X_train, X_test, Y_btc_train, Y_btc_test = train_test_split(X, Y_btc, test_size=0.2, random_state=42)
X_train, X_test, Y_eth_train, Y_eth_test = train_test_split(X, Y_eth, test_size=0.2, random_state=42)

# Step 4: Train the Machine Learning model
btc_model = LinearRegression()
eth_model = LinearRegression()

btc_model.fit(X_train, Y_btc_train)
eth_model.fit(X_train, Y_eth_train)

# Step 5: Test the model & check accuracy
btc_predictions = btc_model.predict(X_test)
eth_predictions = eth_model.predict(X_test)

btc_error = mean_absolute_error(Y_btc_test, btc_predictions)
eth_error = mean_absolute_error(Y_eth_test, eth_predictions)

print(f"✅ Model trained successfully!")
print(f"📊 Bitcoin Prediction Error: ${btc_error:.2f}")
print(f"📊 Ethereum Prediction Error: ${eth_error:.2f}")

# Step 6: Save the trained models
with open("crypto_model.pkl", "wb") as model_file:
    pickle.dump({"btc_model": btc_model, "eth_model": eth_model}, model_file)

print(f"✅ Model saved as 'crypto_model.pkl'")

# Step 7: Visualize results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(X_test, Y_btc_test, color="blue", label="Actual Price")
plt.plot(X_test, btc_predictions, color="red", linewidth=2, label="Predicted Price")
plt.title("Bitcoin Price Prediction")
plt.xlabel("Timestamp")
plt.ylabel("Price (USD)")
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(X_test, Y_eth_test, color="green", label="Actual Price")
plt.plot(X_test, eth_predictions, color="red", linewidth=2, label="Predicted Price")
plt.title("Ethereum Price Prediction")
plt.xlabel("Timestamp")
plt.ylabel("Price (USD)")
plt.legend()

plt.show()
