import pandas as pd
from datetime import datetime
from finnhub_service import get_client


def build_macd_histogram(*args):
    response = get_client(*args)
    if not response:
        return False
    data_frame = pd.DataFrame({'date': [datetime.utcfromtimestamp(date) for date in response['t']],
                               'low': response['l'], 'high': response['h'], 'open': response['o'], 'close': response['c']})
    exp_fast = data_frame.close.ewm(span=12, adjust=False).mean()
    exp_slow = data_frame.close.ewm(span=26, adjust=False).mean()
    histogram = exp_fast - exp_slow
    signal_line = histogram.ewm(span=9, adjust=False).mean()
    return histogram, signal_line, data_frame