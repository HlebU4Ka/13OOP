import requests, json
from datetime import datetime
import os

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")

def get_currency_rate(base):
    pass
def save_to_json(data):
    pass
def main():
    while True:
        currency = input("Введите название валюты (USD или EUR) ")
        if currency not in ("USD", "EUR"):
            print("Некоректный ввод")
            continue
            # При не выполненных условиях код ниже пропуститься,
            # и условие для входа повторится сначала.


        rate = get_currency_rate(currency)
        linestamp = datetime.now()

        print(f"Курс {currency} к рублю {rate}")
        data = {"currency": currency, "rate": rate, "linestamp": linestamp}
        save_to_json(data)

        choice = input("Выберете дайствие: 1 - продолжить, 2 - выйти")
        if choice == "1":
            continue
        elif choice == "2":
            break
        else:
            print("Некорректный ввод")



if __name__ == '__main__':
    main()