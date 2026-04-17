import logging

import json

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/utils.log', mode = 'w')
file_formater = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: - %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)

def transaction_data(path: str) -> list:
    """Функция принимает путь к JSON файлу и выводит его содержимое"""
    logger.debug('Получение пути к файлу JSON')
    try:
        with open(path) as f:
            operations = json.load(f)
            if isinstance(operations, list):
                logger.info('Файл успешно распознан как JSON')
                return operations
            else:
                logger.warning('Данные не являются - JSON')
                return []
    except FileNotFoundError:
        logger.error('Файл по заданному пути не найден')
        return []
    except json.JSONDecodeError:
        logger.error('Ошибочная структура данных в файле')
        return []

print(transaction_data('../data/operation.json'))
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
