import re
from collections import Counter

from src.generators import transactions


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция, которая будет принимать список словарей с данными о банковских операциях
    и строку поиска, а возвращать список словарей"""
    result = []
    for item in data:
        if re.search(search, item.get("description", ""), re.IGNORECASE):
            result.append(item)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Подсчитывает количество операций по категориям заданным в списке"""
    descriptions = []
    for transaction in transactions:
        if "description" in transaction and transaction["description"] is not None:
            descriptions.append(transaction["description"])
    counter = Counter(descriptions)
    result = {category: counter.get(category, 0) for category in categories}
    return result


# if __name__ == '__main__':
# print(process_bank_search(transactions,"Перевод организации"))
# print(process_bank_operations(transactions,["Перевод со счета на счет", "Перевод организации"]))
