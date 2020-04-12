import os
import csv


def exchange_transaction(direction, date, o, c):
    if direction:
        file_writer('BUY', date, o, c)
    else:
        file_writer('SELL', date, o, c)


def file_writer(direction, date, o, c):
    fields = locals()
    file_path = os.path.join(os.path.dirname(__file__), 'test.csv')
    if not os.path.isfile(file_path):
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields.keys())
            writer.writeheader()
            writer.writerow(fields)
    else:
        with open(file_path, 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fields.values())
