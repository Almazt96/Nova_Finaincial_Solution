import talib
import numpy as np
import pandas as pd
import pandas_ta as ta

""" # Example data: Replace with actual stock data (e.g., from YFinance)
close_prices = np.array([298.36, 296.24, 296.71, 299.44, 302.12, 301.36])

# Calculate Simple Moving Average (SMA) for a 3-day period
sma = talib.SMA(close_prices, timeperiod=3)
print("SMA:", sma)

# Calculate Relative Strength Index (RSI) for a 14-day period
rsi = talib.RSI(close_prices, timeperiod=14)
print("RSI:", rsi) """

# Sample DataFrame with Close prices
data = pd.DataFrame({
    'Close': [45.15, 46.23, 47.65, 48.23, 49.54, 48.98, 47.89, 47.01, 48.10, 48.67]
})

# Adding RSI indicator
data['RSI'] = ta.rsi(data['Close'], length=14)

print(data)