def filter(data, currency):
    """Функция фильтрует корректные данные для выборки в зависимости от типа вложенности данных"""
    filtered_list = []
    for transaction in data:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            filtered_list.append(transaction)
        elif transaction.get("currency_code") == currency:
            filtered_list.append(transaction)

    return filtered_list
