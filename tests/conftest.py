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

@pytest.fixture()
def filter_list():
    return [
        {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]



