import talib
import numpy as np

# Example data: Replace with actual stock data (e.g., from YFinance)
close_prices = np.array([298.36, 296.24, 296.71, 299.44, 302.12, 301.36])

# Calculate Simple Moving Average (SMA) for a 3-day period
sma = talib.SMA(close_prices, timeperiod=3)
print("SMA:", sma)

# Calculate Relative Strength Index (RSI) for a 14-day period
rsi = talib.RSI(close_prices, timeperiod=14)
print("RSI:", rsi)
