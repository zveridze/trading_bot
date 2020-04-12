from datetime import datetime
import settings
import requests
from requests.exceptions import ConnectionError
from json.decoder import JSONDecodeError


def get_client(ticker=None, start=None, end=None):
    if not settings.API_KEY:
        raise ValueError('Api-key for "Finnhub" does not set up. Please set up api-key.')
    if not ticker:
        raise ValueError('Ticker does not define! Please set up ticker.')
    params = {
        'symbol': ticker,
        'resolution': 60,
        'from': datetime.timestamp(datetime.strptime(start, '%Y-%m-%d')) if start else '1514764800',
        'to': datetime.timestamp(datetime.strptime(end, '%Y-%m-%d')) if end else datetime.timestamp(datetime.now()),
        'token': settings.API_KEY
    }

    try:
        r = requests.get(
            url='https://finnhub.io/api/v1/stock/candle',
            params=params
        )
        if r.json()['s'] == 'no_data':
            raise ValueError('No data for this ticker. Please choose another one.')
        return r.json()
    except JSONDecodeError:
        print('Something went wrong. Please try again later.')
        return None
    except ConnectionError:
        print('Service unavailable. Please try again later.')
        return None
