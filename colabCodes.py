# prompt: Predict BTC with LSTM using Tensorflow gpu with python

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load the Bitcoin data
df = pd.read_csv('btc.csv')

# Split the data into training and testing sets
train_size = int(len(df) * 0.8)
train_data = df[:train_size]
test_data = df[train_size:]

# Scale the data
scaler = MinMaxScaler()
train_data = scaler.fit_transform(train_data['Close'].values.reshape(-1, 1))
test_data = scaler.transform(test_data['Close'].values.reshape(-1, 1))

# Create the LSTM model
model = keras.Sequential([
  layers.LSTM(units=50, return_sequences=True, input_shape=(train_data.shape[1], 1)),
  layers.LSTM(units=50),
  layers.Dense(units=1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(train_data, train_data, epochs=5, batch_size=32)

# Evaluate the model
test_predict = model.predict(test_data)
test_predict = scaler.inverse_transform(test_predict)
test_y = scaler.inverse_transform(test_data)

# Plot the results
plt.plot(test_y, label='True')
plt.plot(test_predict, label='Predicted')
plt.legend()
plt.show()
