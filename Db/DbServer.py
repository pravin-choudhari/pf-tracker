import mysql.connector


class DbServer:
    def __init__(self, user, password, host, database):
        self.db_config = {
            'user': user,
            'password': password,
            'host': host,
            'database': database
        }
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(**self.db_config)
        self.cursor = self.connection.cursor()
        print("Connected to database.")


    def insert_price(self, symbol, exchange, date, close_price):
        insert_query = """
        INSERT INTO stock_prices (symbol, exchange, date, close_price)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE close_price = VALUES(close_price)
        """
        self.cursor.execute(insert_query, (symbol, exchange, date, close_price))

    def commit(self):
        self.connection.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Database connection closed.")