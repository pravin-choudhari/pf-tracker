import yfinance as yf
from nsetools import Nse
import pandas as pd
from datetime import datetime, timedelta

class StockDataFetcher:
    def __init__(self):
        self.nse = Nse()
        self.end_date = datetime.now()
        self.start_date = self.end_date - timedelta(days=30)

    def fetch_nse_data(self, stock):
        #nse_stocks = self.nse.get_stock_codes()
        #nse_stocks = [symbol for symbol in nse_stocks if symbol.isalpha()]
        stock_data = {}
        nse_stocks = [stock]
        
        for symbol in nse_stocks:
            try:
                ticker = yf.Ticker(f"{symbol}.NS")
                hist = ticker.history(start=self.start_date, end=self.end_date)
                stock_data[symbol] = hist['Close']
            except Exception as e:
                print(f"Error fetching data for {symbol}: {e}")
        
        return stock_data

    def fetch_bse_data(self):
        bse_stocks = ['RELIANCE', 'TCS']  # Replace with desired BSE symbols
        bse_data = {}
        
        for symbol in bse_stocks:
            try:
                quote = self.nse.get_quote(symbol)
                close_price = quote.get('closePrice')
                if close_price:
                    bse_data[symbol] = close_price
            except Exception as e:
                print(f"Error fetching data for {symbol}: {e}")
        
        return bse_data

