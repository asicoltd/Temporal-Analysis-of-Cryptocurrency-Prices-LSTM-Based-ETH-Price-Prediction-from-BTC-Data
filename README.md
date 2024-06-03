Ethereum Price Prediction Using LSTM

This repository contains Python code for predicting Ethereum (ETH) prices based on Bitcoin (BTC) prices using Long Short-Term Memory (LSTM) neural networks.

Features:

- Data Collection: Historical price data for both BTC and ETH is collected from reliable sources like cryptocurrency exchanges or financial data providers such as Binance, CoinMarketCap, CoinGecko, or Yahoo Finance.
- Dataset Description and Sources of Data: The dataset includes BTC and ETH price data with information about the time range, frequency, and sources.
- Data Preprocessing: BTC and ETH price data are loaded from CSV files, merged, and preprocessed. Columns are renamed for clarity, and data is normalized to ensure similar scales.
- Feature Engineering: Lagged features for BTC prices and technical indicators (like moving averages, RSI, MACD) are computed based on BTC prices and used as additional features.
- Model Selection: An LSTM neural network architecture is chosen to predict ETH prices based on BTC prices.
- Model Training: The LSTM model is trained using a defined training strategy, optimizer, learning rate, batch size, and number of epochs. Hyperparameters are tuned using techniques like Grid Search or Random Search.
- Model Evaluation: The model's performance is evaluated using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), or Root Mean Squared Error (RMSE). Cross-validation is performed to ensure model robustness.
- Challenges Faced: Any challenges encountered during the project, such as data preprocessing issues, model convergence problems, or difficulties in optimizing hyperparameters, are described.
- Recommendations for Future Works/Improvement: Suggestions for future research or improvements to the model, such as exploring additional features, experimenting with different model architectures, or incorporating external factors that may influence ETH prices, are provided.

Usage:

1. Clone the Repository:

   git clone https://github.com/asicoltd/Time-series-forecasting.git

2. Navigate to the Project Directory:

   cd Time-series-forecasting

3. Prepare Data:

   - Place your BTC and ETH price data CSV files in the project directory with the following naming convention:
     - BTC5m.csv for Bitcoin data
     - ETH5m.csv for Ethereum data

4. Run the Python Script:

   python B2LpredictV2.ipynb

   This script will train the LSTM model on the provided data and generate predictions for Ethereum prices.

Requirements:

- Python 3.x
- pandas
- matplotlib
- numpy
- torch
- scikit-learn

Additional Notes:

- You can adjust hyperparameters and model architecture in the script according to your requirements.
- Ensure that your CSV files contain columns named 'Date' and 'close' for both BTC and ETH data.
