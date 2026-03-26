import pytest

@pytest.fixture()
def card_num():
    return '7000 79** **** 6361'

@pytest.fixture()
def invoice_num():
    return '**4305'

@pytest.fixture()
def mask_account():
    return 'Maestro 1596 83** **** 5199'

@pytest.fixture()
def mask_data():
    return '11.03.2024'