transactions =  [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 123456789,
        "state": "EXECUTED",
        "date": "2026-03-30T20:06:51.206887",
        "operationAmount": {"amount": "65765.93", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {},  # Пустая транзакция
    {
        "id": 142264269,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]
def filter_by_currency(transactions: list[dict], currency: str) -> list[dict]:
    """ Функция возвращает транзакции в которых валюта соответствует заданной"""
    found = False  # Флаг для отслеживания транзакций
    for transaction in transactions:
        if (transaction and
                transaction.get("operationAmount", {}).get("currency", {}).get("name") == currency):
            found = True
            yield transaction

    if not found:
        yield "Нет транзакции"  #  Строка, если ничего не найдено

def transaction_descriptions(transactions: list[dict]) -> str:
    for transaction in transactions:
        if not transaction:
            yield 'Отсутствует транзакция' #проверка пустой транзакции
            continue
        description = transaction.get("description")
        yield description if description else 'Отсутствует описание'

    if not transactions: #проверка пустого списка
        yield "Транзакции отсутствуют"


def card_number_generator(start: int, stop: int) -> str:
    """генератор выдаёт номера карт в формате XXXX XXXX XXXX XXXX"""
    for num in range(start, stop + 1):
        card_num = str(num).zfill(16)
        yield f'{card_num[:4]} {card_num[5:9]} {card_num[8:12]} {card_num[12:]}'

for card_number in card_number_generator(1, 5):

    print(card_number)
