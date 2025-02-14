document.getElementById("predictBtn").addEventListener("click", function () {
  fetch("/predict")  // Fetch from your Render server
      .then(response => response.json())
      .then(data => {
          // Update the DOM with predicted prices
          document.getElementById("btc-price").innerText = data.Bitcoin["Predicted Price"].toFixed(2);
          document.getElementById("eth-price").innerText = data.Ethereum["Predicted Price"].toFixed(2);
          document.getElementById("timestamp").innerText = data.Timestamp;
      })
      .catch(error => {
          console.error("Error fetching data:", error);
          alert("Failed to fetch predictions. Check the console for details.");
      });
});