from generators import transactions
from search import process_bank_search, process_bank_operations


def test_search():
    assert process_bank_search(transactions, "Перевод организации") == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
         'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}]


def test_bank_operation():
    assert process_bank_operations(transactions, ["Перевод со счета на счет", "Перевод организации"]) == {
        'Перевод со счета на счет': 2, 'Перевод организации': 1}
