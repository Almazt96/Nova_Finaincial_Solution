"Data Analysis and Visualization"
import matplotlib.pyplot as plt
import pandas as pd

# Load data from a file
stock_data = pd.read_csv("../data/raw/raw_AAPL_historical_data.csv")

# Plot stock price data and the moving average
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label='Close Price')
plt.plot(stock_data['Close'].rolling(window=20).mean(), label='20-Day Moving Average', color='red')
plt.title('AAPL Stock Price and 20-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.show()
