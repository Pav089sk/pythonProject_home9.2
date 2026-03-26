from src.widget import mask_account_card
# from src.widget import get_date

def test_mask_account(mask_account):
    assert mask_account_card('Maestro 1596837868705199') == mask_account

def test_mask_account_invoice():
    assert mask_account_card("Счет 35383033474447895560") == 'Счет **5560'


