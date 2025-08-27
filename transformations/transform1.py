sma_20 = data['Close'].rolling(window=20).mean()
print(sma_20)
sma_50 = data['Close'].rolling(window=50).mean()
print(sma_50)
