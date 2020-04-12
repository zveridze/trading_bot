import argparse
from macd import build_macd_histogram
from utils import exchange_transaction
from datetime import datetime


def data_frame_processing(histogram, signal_line, data_frame, is_bigger):
    for his, sl, df in zip(histogram, signal_line, data_frame.iterrows()):
        if sl > his and not is_bigger:
            exchange_transaction(is_bigger, df[1].date, df[1].open, df[1].close)
            is_bigger = True
        if sl < his and is_bigger:
            exchange_transaction(is_bigger, df[1].date, df[1].open, df[1].close)
            is_bigger = False


def start_monitoring(*args):
    is_bigger = None
    try:
        histogram, signal_line, data_frame = build_macd_histogram(*args)
        counter = 0
        while histogram[counter] == signal_line[counter]:
            counter += 1
        else:
            if histogram[counter] > signal_line[counter]:
                is_bigger = False
            elif histogram[counter] < signal_line[counter]:
                is_bigger = True

        updated_data_frame = data_frame.drop(range(counter))

        data_frame_processing(histogram[counter:], signal_line[counter:], updated_data_frame, is_bigger)
    except TypeError:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', help='Stock ticker.')
    parser.add_argument('-s', help='Start date. Set up by default as 2018-01-01.')
    parser.add_argument('-e', help='End date. Set up by default as today.')
    args = parser.parse_args()
    try:
        datetime.strptime(args.s, '%Y-%m-%d')
        datetime.strptime(args.e, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Incorrect date format! Please use format YYYY-mm-dd.')
    start_monitoring(args.t, args.s, args.e)
