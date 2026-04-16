import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY =  os.getenv('API_KEY')

def transaction_amount(operation):
    """Функция для конвертации суммы транзакции в транзакцию в рублях"""
    fr = operation.get("operationAmount", {}).get("currency", {}).get("code")
    am = operation.get("operationAmount", {}).get("amount")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={fr}&amount={am}"

    payload = {}
    headers = {
        "apikey": API_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text
    return response.json().get('result')

# # if __name__ == '__main__':
#     print(transaction_amount(
#         {
#             "id": 41428829,
#             "state": "EXECUTED",
#             "date": "2019-07-03T18:35:29.512364",
#             "operationAmount": {
#                 "amount": "8221.37",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "MasterCard 7158300734726758",
#             "to": "Счет 35383033474447895560"
#         }
#     ))
