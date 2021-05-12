import requests
import json
from config import keys

class ConverterException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if quote == base:
            raise ConverterException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConverterException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConverterException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConverterException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?symbols={quote_ticker}&base={base_ticker}')
        result = float(json.loads(r.content)['rates'][base_ticker])*amount


        return round(result, 3)