import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions

@pytest.mark.parametrize('currency, result',
                         [
                             (
                                     "USD",
                                     [
                                         {
                                             "id": 939719570,
                                             "state": "EXECUTED",
                                             "date": "2018-06-30T02:08:58.425572",
                                             "operationAmount": {"amount": "9824.07",
                                                                 "currency": {"name": "USD", "code": "USD"}},
                                             "description": "Перевод организации",
                                             "from": "Счет 75106830613657916952",
                                             "to": "Счет 11776614605963066702",
                                         },
                                         {
                                             "id": 142264269,
                                             "state": "EXECUTED",
                                             "date": "2019-04-04T23:20:05.206878",
                                             "operationAmount": {"amount": "79114.93",
                                                                 "currency": {"name": "USD", "code": "USD"}},
                                             "description": "Перевод со счета на счет",
                                             "from": "Счет 19708645243227258542",
                                             "to": "Счет 75651667383060284188",
                                         },
                                     ],
                             ),
                             (
                                     "EUR",
                                     [
                                         {
                                             "id": 123456789,
                                             "state": "EXECUTED",
                                             "date": "2026-03-30T20:06:51.206887",
                                             "operationAmount": {"amount": "65765.93",
                                                                 "currency": {"name": "EUR", "code": "EUR"}},
                                             "description": "Перевод со счета на счет",
                                             "from": "Счет 19708645243227258542",
                                             "to": "Счет 75651667383060284188",
                                         }
                                     ],
                             ),
                             ("RUR", ["Нет транзакции"]),
                         ],
                         )
def test_filter_by_currency(currency, result):
    res = list(filter_by_currency(transactions, currency))
    assert res == result

@pytest.fixture
def test_transaction():
    return[

                                         {
                                             "id": 939719570,
                                             "state": "EXECUTED",
                                             "date": "2018-06-30T02:08:58.425572",
                                             "operationAmount": {"amount": "9824.07",
                                                                 "currency": {"name": "USD", "code": "USD"}},
                                             "description": "Перевод организации",
                                             "from": "Счет 75106830613657916952",
                                             "to": "Счет 11776614605963066702",
                                         },
                                         {
                                             "id": 142264269,
                                             "state": "EXECUTED",
                                             "date": "2019-04-04T23:20:05.206878",
                                             "operationAmount": {"amount": "79114.93",
                                                                 "currency": {"name": "USD", "code": "USD"}},
                                             "description": "Перевод со счета на счет",
                                             "from": "Счет 19708645243227258542",
                                             "to": "Счет 75651667383060284188",
                                         },
                              {
                                             "id": 123456789,
                                             "state": "EXECUTED",
                                             "date": "2026-03-30T20:06:51.206887",
                                             "operationAmount": {"amount": "65765.93",
                                                                 "currency": {"name": "EUR", "code": "EUR"}},
                                             "description": "",
                                             "from": "Счет 19708645243227258542",
                                             "to": "Счет 75651667383060284188",
                                         }]


@pytest.fixture
def expected():
    return ["Перевод организации", "Перевод со счета на счет", "Отсутствует описание"]

def test_transaction_type(test_transaction, expected):
    descriptions = list(transaction_descriptions(test_transaction))
    assert descriptions == expected

@pytest.fixture
def card_number_test():
    return {
        "start": 1,
        "stop": 5,
        "expected": [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005",
        ],
    }


@pytest.fixture
def empty_card_number_test():
    return {
        "start": 6,
        "stop": 5,  # Пустой диапазон, старт больше конца
        "expected": [],  # Ожидаемое значение пустой коллекции
    }


# Тест функции генератора
def test_card_number_generator(card_number_test):
    start = card_number_test["start"]
    stop = card_number_test["stop"]
    expected = card_number_test["expected"]

    # Генерация номеров карт с помощью генератора
    result = list(card_number_generator(start, stop))

    # Проверка соответствия с ожидаемым значением
    assert result == expected


# Тест пустого диапазона генератора
def test_empty_card_number_generator(empty_card_number_test):
    start = empty_card_number_test["start"]
    stop = empty_card_number_test["stop"]
    expected = empty_card_number_test["expected"]

    # Генерация номеров карт с помощью генератора
    result = list(card_number_generator(start, stop))

    # Проверка соответствия с ожидаемым значением
    assert result == expected