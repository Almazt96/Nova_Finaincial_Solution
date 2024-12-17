import yfinance as yf
import pandas as pd

# Download stock data for AAPL and MSFT
tickers = ['AAPL', 'MSFT']
data = yf.download(tickers, start='2020-01-01', end='2024-01-01')['Adj Close']
# Calculate daily returns
returns = data.pct_change()
# Calculate the correlation matrix
correlation_matrix = returns.corr()
print(correlation_matrix)
import seaborn as sns
import matplotlib.pyplot as plt

# Plot the heatmap of correlation
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix: AAPL vs MSFT')
plt.show()
import pynance as pn
prices = pn.data.get_prices(['AAPL', 'MSFT'], start="2020-01-01")
print(prices)
