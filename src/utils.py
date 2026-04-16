import json


def transaction_data(path: str) -> list:
    """Функция принимает путь к JSON файлу и выводит его содержимое"""
    try:
        with open(path) as f:
            operations = json.load(f)
            if isinstance(operations, list):
                return operations
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


# def currency_choise(transactions_list):
#     """Функция получает транзакцию из списка транзакций
#      валюта которой не рубли"""
#     for operation in transactions_list:
#         if operation["operationAmount"]["currency"]["code"] != "RUB":
#             a = transaction_amount(operation)
#             return a
#
# print(currency_choise([
#         {
#             "operationAmount": {
#                 "currency": {"code": "USD"}
#             }
#         },
#         {
#             "operationAmount": {
#                 "currency": {"code": "RUB"}
#             }
#         }
#     ]))
