import random
import time
import datetime as dt


class StockExchangeProvider:
    num_quotes: int
    is_connected: bool = False

    def __init__(self):
        self.num_quotes = 0
        self.symbols = []

    def connect(self, user, password) -> bool:
        if user == 'ploni' and password == 'Aa123456':
            self.is_connected = True
            return True
        return False

    def receive_quotes(self, symbols: list, callback):
        """
        :param symbols: list of symbols
        :param callback: the func should be with the following signature: func(quote)-> void
        :return:
        """
        self.callback = callback
        self.symbols = symbols

    # implemented. after calling this func you start receiving data and send to callback
    def start(self):
        if not any(self.symbols):
            raise Exception('no symbols were supplied')
        if self.callback is None:
            raise Exception('no callback was supplied')
        if self.is_connected:
            while True:
                for sym in self.symbols:
                    self.callback({time: dt.datetime.now(), 'symbol': sym, 'price': random.randint(1, 100)})
                    time.sleep(0.10)
                    self.num_quotes += 1
                if self.num_quotes % 50 == 0:
                    self.is_connected = False
                    self.callback = None
                    raise Exception('connection error')
        raise Exception('not connected to stock exchange')
