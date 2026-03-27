import pytest
from src.widget import mask_account_card
from src.widget import get_date

def test_mask_account(mask_account):
    assert mask_account_card('Maestro 1596837868705199') == mask_account

def test_mask_account_invoice():
    assert mask_account_card('Счет 35383033474447895560') == 'Счет **5560'

def test_mask_account_2():
    assert mask_account_card('MasterCard 7158300734726758') == 'MasterCard 7158 30** **** 6758'

@pytest.mark.parametrize("number, result", [("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229")])
def test_correct_account(number: str, result: str) -> None:
    assert mask_account_card(number) == result

def test_mask_account_empty():
    assert mask_account_card('') == 'Информация отсутствует'

def test_mask_account_empty2():
    assert mask_account_card(' ') == 'Информация отсутствует'

def test_mask_data(mask_data):
    assert get_date('2024-03-11T02:26:18.671407') == mask_data

def test_mask_data_2():
    assert get_date('2026-12-10T02:26:18.671407') == '10.12.2026'

def test_mask_data_empty():
    assert get_date('') == ''
