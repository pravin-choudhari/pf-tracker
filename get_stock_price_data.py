from Db.DbServer import DbServer
from MktData.stockpriceupdater import StockPriceUpdater

def main():
    # Database credentials
    db = DbServer(user='root', password='password', host='localhost', database='stock_data')
    
    # Connect and prepare database
    db.connect()
    #db.create_table()

    # Update stock prices
    updater = StockPriceUpdater(db)
    updater.update_nse_prices()
    #updater.update_bse_prices()

    # Close database connection
    db.close()


if __name__ == "__main__":
    main()