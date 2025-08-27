tickers = ["AAPL", "NVDA", "TSLA", "GOOGL", "MSFT"]
period = "5y"
print("Downloading stock data...")
data_ohlc = yf.download(tickers, period=period)
close_prices = data_ohlc['Close']
print("✅ Data downloaded.")

sma_20 = close_prices.rolling(window=20).mean()
sma_50 = close_prices.rolling(window=50).mean()
sma_df = pd.concat([sma_20.add_suffix('_sma20'), sma_50.add_suffix('_sma50')], axis=1)
daily_returns = close_prices.pct_change()
weights = py.array([0.20, 0.20, 0.20, 0.20, 0.20])
portfolio_daily_returns = daily_returns.dot(weights)
portfolio_df = pd.DataFrame((1 + portfolio_daily_returns).cumprod(), columns=['cumulative_return'])

cumulative_returns_individual = (1 + daily_returns).cumprod()
total_returns = cumulative_returns_individual.iloc[-1]

gainers_losers_df = pd.DataFrame(total_returns.sort_values(ascending=False), columns=['total_return_factor'])

print("✅ All calculations are complete.")


db_user = 'postgres'
db_password = 'post123'
db_host = 'localhost'
db_port = '5432'
db_name = 'postgres'

safe_password = quote_plus(db_password)


connection_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(connection_string)
print("Database engine created.")

schema_name = 'Stockprice' 

try:
    print(f"\nLoading data into schema: '{schema_name}'...")
    
    # Load SMAs
    sma_df.to_sql('simple_moving_averages', engine, schema=schema_name, if_exists='replace', index=True)
    print(f"✅ Table 'simple_moving_averages' loaded.")
    
    # Load Portfolio Performance
    portfolio_df.to_sql('portfolio_performance', engine, schema=schema_name, if_exists='replace', index=True)
    print(f"✅ Table 'portfolio_performance' loaded.")

    # Load Gainers/Losers Ranking
    gainers_losers_df.to_sql('stock_performance_ranking', engine, schema=schema_name, if_exists='replace', index=True)
    print(f"✅ Table 'stock_performance_ranking' loaded.")
    
    print("\nAll data has been successfully loaded into your PostgreSQL schema.")

except Exception as e:
    print(f"🔥 An error occurred: {e}")
  time;