from cProfile import run
from dataclasses import dataclass
import requests
running = True
url = 'https://api.exchangerate-api.com/v4/latest/USD'

class realTimeConverter():
    def __init__(self):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        if from_currency != 'USD':
            amount = amount / self.currencies[to_currency]
        output_value = amount * self.currencies[to_currency]

        print(output_value)

while running:
    from_currency = input("Wpisz walute początkową w formacie PLN, USD, GBP itp. \nNaciśnij Ctrl + C żeby zakończyć").upper()     
    to_currency = input("wpisz walute końcową").upper()
    amount = 24

    converter = realTimeConverter()
    converter.convert(from_currency, to_currency, amount)
    print()