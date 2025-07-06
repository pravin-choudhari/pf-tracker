from .stockdatafetcher import StockDataFetcher
import pandas as pd

class StockPriceUpdater:
    def __init__(self, db):
        self.db = db
        self.data_fetcher = StockDataFetcher()

    def update_nse_prices(self):
        nse_stocks = self.get_all_nse_tickers()
        #nse_data = self.data_fetcher.fetch_nse_data()
        for stock in nse_stocks:
            print(f"updating data for NSE stock: {stock}")
            nse_data = self.data_fetcher.fetch_nse_data(stock)
            for symbol, prices in nse_data.items():
                for date, close_price in prices.items():
                    self.db.insert_price(symbol, 'NSE', date.date(), close_price)
            self.db.commit()
        
        #for symbol, prices in nse_data.items():
        #    for date, close_price in prices.items():
        #        self.db.insert_price(symbol, 'NSE', date.date(), close_price)
        #self.db.commit()
        print("NSE data updated.")

    def update_bse_prices(self):
        bse_data = self.data_fetcher.fetch_bse_data()
        
        for symbol, close_price in bse_data.items():
            self.db.insert_price(symbol, 'BSE', self.data_fetcher.end_date.date(), close_price)
        self.db.commit()
        print("BSE data updated.")

    def get_all_nse_tickers(self):
        try:    
            data = pd.read_csv('./data/EQUITY_L.csv', usecols=['SYMBOL'])
            #rslt_data = data[~data['SYMBOL'].str.isalpha()]
            data_list = list(data['SYMBOL'])
            print(data_list)
            #nse_stocks = [symbol for symbol in data if symbol.isalpha()]
            return data_list
        except FileNotFoundError as e:
            print("File not found: {e}")
        except ValueError as e:
            print("Value error: {e}")

