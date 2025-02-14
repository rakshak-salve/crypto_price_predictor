# Import required libraries 
import requests  # To fetch data from API
import csv       # To store data in a CSV file
from datetime import datetime  # To track the date & time of each entry

# Define the API URL for CoinGecko
API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

# Function to fetch real-time Bitcoin & Ethereum prices
def get_crypto_prices():
    try:
        # Fetch data from CoinGecko API
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise error for failed requests
        data = response.json()

        # Extract Bitcoin and Ethereum prices
        btc_price = data["bitcoin"]["usd"]
        eth_price = data["ethereum"]["usd"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current date & time

        # Print the prices in a clean format
        print(f"💰 {timestamp} - Bitcoin: ${btc_price}, Ethereum: ${eth_price}")

        # Save the data into a CSV file
        save_to_csv(timestamp, btc_price, eth_price)

    except requests.exceptions.RequestException as e:
        print("❌ Error fetching data:", e)

# Function to store data in a CSV file
def save_to_csv(timestamp, btc_price, eth_price):
    file_path = "crypto_prices.csv"  # File name

    # Open the file in 'append' mode, so new data is added at the bottom
    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        
        # If it's the first entry, write column headers
        if file.tell() == 0:
            writer.writerow(["Timestamp", "Bitcoin Price (USD)", "Ethereum Price (USD)"])
        
        # Write the current data row
        writer.writerow([timestamp, btc_price, eth_price])

    print("✅ Data saved to crypto_prices.csv")

# Run the function to fetch prices & store them
get_crypto_prices()
