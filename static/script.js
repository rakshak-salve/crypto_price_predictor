document.getElementById("predictBtn").addEventListener("click", function () {
    fetch("http://127.0.0.1:5000/predict")
        .then(response => response.json())
        .then(data => {
            document.getElementById("btcPrice").innerText = data.Bitcoin["Predicted Price"].toFixed(2);
            document.getElementById("ethPrice").innerText = data.Ethereum["Predicted Price"].toFixed(2);
            document.getElementById("timestamp").innerText = data.Timestamp;
        })
        .catch(error => console.error("Error fetching data:", error));
});
