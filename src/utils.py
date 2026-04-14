import json

def transaction_data(path: str) -> list:
    """Функция принимает путь к JSON файлу и выводит его содержимое"""
    try:
       with open(path) as f:
           operations = json.load(f)
           if isinstance(operations, list):
               return operations
    except FileNotFoundError:
       return []
    except json.JSONDecodeError:
        return []

transactions_list = transaction_data('../data/operations.json')


