from src.masks import get_mask_card_number
from src.masks import get_mask_account


def test_mask_card_num(card_num):
    assert get_mask_card_number(7000792289606361) == card_num

def test_mask_account(invoice_num):
    assert get_mask_account(73654108430135874305) == invoice_num

def test_mask_card_num_outsize():
    assert get_mask_card_number(1237000792289606361) == 'Неверный номер карты'

def test_mask_card_num_resize():
    assert get_mask_card_number(70007922896063) == 'Неверный номер карты'

def test_mask_card_num_empty():
    assert get_mask_card_number('') == 'Неверный номер карты'

def test_get_mask_account_outsize():
    assert get_mask_account(736541084301358743050101) == 'Неверный номер счета'

def test_get_mask_account_resize():
    assert get_mask_account(7365410843013587) == 'Неверный номер счета'