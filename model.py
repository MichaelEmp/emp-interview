import random
from typing import Dict


class Model:
    def predict(self, calced_data: dict):
        """
        :param calced_data: symbol, calculated data for symbol
        :return: The symbol to buy immediately and the num of seconds you need wait until you sell the symbol
        """
        index = random.randint(0, len(calced_data)-1)
        return list(calced_data)[index], random.randint(1, 40)
