tickers = ["AAPL", "NVDA", "TSLA", "GOOGL", "MSFT"]
data = yf.download(tickers, period="5y")['Close']
daily_returns = data.pct_change()

cumulative_returns_individual = (1 + daily_returns).cumprod()
total_returns = cumulative_returns_individual.iloc[-1]

sorted_returns = total_returns.sort_values(ascending=True)

top_gainers = sorted_returns.tail(3)
top_losers = sorted_returns.head(3)

print("--- Total Return Over 5 Years (1 = 100% gain) ---")
print(sorted_returns)

print("\n--- Top 3 Gainers 🚀 ---")
print(top_gainers)

print("\n--- Top 3 Losers 📉 ---")
print(top_losers)