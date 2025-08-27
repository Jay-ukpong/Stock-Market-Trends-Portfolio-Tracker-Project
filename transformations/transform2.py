tickers = ["AAPL", "NVDA", "TSLA", "GOOGL", "MSFT"]
data = yf.download(tickers, period="5y")['Close']
daily_returns = data.pct_change()
weights = py.array([0.20, 0.20, 0.20, 0.20, 0.20])
portfolio_daily_returns = daily_returns.dot(weights)
cumulative_returns = (1 + portfolio_daily_returns).cumprod()
print("--- Last 5 Days of Portfolio Performance ---")
print(cumulative_returns.tail())
