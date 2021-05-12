import requests
import json
from config import keys, API_access_key, url

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

        r = requests.get(f'{url}?access_key={API_access_key}&symbols={quote_ticker}')
        r1 = requests.get(f'{url}?access_key={API_access_key}&symbols={base_ticker}')
        if base =='EUR':
            total_base = json.loads(r.content)['rates'][quote_ticker]*amount

        else:
            A = json.loads(r1.content)['rates'][base_ticker]
            B = json.loads(r.content)['rates'][quote_ticker]
            total_base = (B/A) * amount


        return round(total_base, 2)