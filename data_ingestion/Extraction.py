import yfinance as yf
import pandas as pd
import numpy as py
from sqlalchemy import create_engine
from urllib.parse import quote_plus

tickers=["AAPL","NVDA","TSLA","GOOGL","MSFT"]
data=yf.download(tickers,period="5y")
pd.set_option('display.max_columns', None)
print(data.head())
