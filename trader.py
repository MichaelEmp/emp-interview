import random
import time
from typing import List


class Trader:
    num_of_bought_symbols = 0
    current_gain = 0

    def __init__(self, symbols: List[str]):
        self.symbols = symbols

    def calc(self, aggregated_quotes):
        if len(aggregated_quotes) == len(self.symbols) * 10:
            time.sleep(0.5)
            return {'std': 2542, 'max': 24, 'min': 2}
        else:
            raise Exception('aggregated quotes must have only 10 elements')

    def sell(self, symbol):
        sell_price = random.randint(1, 100)
        self.current_gain += sell_price
        print(f'The symbol: {symbol} was sold')

    def buy(self, symbol):
        buy_price = random.randint(1, 100)
        self.current_gain -= buy_price
        print(f'The symbol: {symbol} was bought')

    def handle_quotes_data(self, quote):
               """
        Receive quote from stock exchange, aggregate 10 quotes from symbol -> send to get_calced_data in order
        to get the calculated data for prediction -> calls predict -> prints if should be bought.
        You receive quote each millisecond.
        quote is made of : time, symbol, price
       param quote:
       return:"""
