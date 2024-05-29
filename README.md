# Time-series-forecasting
As we know crypto market is highly influenced by BTC and ETH is one of the major cryptos. So I want to predict ETH price from BTC price.


1. Data Collection
    Historical Price Data: Collect historical price data for both BTC and ETH. This data can typically be sourced from cryptocurrency exchanges or financial data providers like CoinMarketCap, CoinGecko, or Yahoo Finance.
    Other Features: Besides price data, consider other relevant features such as trading volume, market sentiment, blockchain metrics (like hash rate and difficulty), and macroeconomic indicators.
2. Data Preprocessing
    Time Alignment: Ensure the data for BTC and ETH are aligned in time.
    Normalization/Standardization: Normalize or standardize the data to ensure that the features have similar scales, which can improve the performance of some machine learning algorithms.
    Handling Missing Values: Address any missing values through imputation or by removing incomplete rows/columns.
3. Feature Engineering
    Lagged Features: Create lagged features for BTC prices. For instance, BTC prices from previous days can be used to predict the current day's ETH price.
    Technical Indicators: Compute technical indicators (like moving averages, RSI, MACD) based on BTC prices and use them as features.
    Sentiment Analysis: Incorporate sentiment analysis data from social media or news sources that relate to BTC and ETH.
4. Model Selection
    Linear Regression: Simple model to understand the linear relationship between BTC and ETH prices.
    Time Series Models: ARIMA, SARIMA, or VAR models that can capture the temporal dependencies.
    Tree-based Models: Decision Trees, Random Forests, Gradient Boosting Machines (GBM), or XGBoost can capture non-linear relationships.
    Neural Networks: Recurrent Neural Networks (RNNs), Long Short-Term Memory networks (LSTMs), or Gated Recurrent Units (GRUs) are suitable for sequential data and can capture complex patterns over time.
    Ensemble Methods: Combining multiple models to improve prediction accuracy.
5. Model Training
    Split the Data: Divide the data into training and testing sets, and possibly a validation set.
    Training: Train selected model on the training data. For time series data, ensure that respect the temporal order during training and evaluation.
    Hyperparameter Tuning: Use techniques like Grid Search or Random Search with cross-validation to tune the model’s hyperparameters.
6. Model Evaluation
    Metrics: Evaluate the model using appropriate metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), or Root Mean Squared Error (RMSE).
    Cross-Validation: Perform cross-validation to ensure the model's robustness and to check for overfitting.
7. Model Deployment
    Prediction: Use the trained model to predict future ETH prices based on the latest BTC prices.
    Monitoring: Continuously monitor the model's performance and retrain it periodically with new data to maintain accuracy.