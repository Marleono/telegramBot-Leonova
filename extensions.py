import requests
import json
from config import keys


class APIException(Exception):
    pass


class Conversion:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException('Невозможно перевести одинаковые валюты')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Валюта {quote} отсутствует')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Валюта {base} отсутствует')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote_ticker}&symbols={base_ticker}')
        total_base = json.loads(r.content)['rates'][keys[base]]

        return total_base*amount
