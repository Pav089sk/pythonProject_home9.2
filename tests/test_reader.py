from unittest.mock import mock_open, patch
import pandas as pd
from src.reader import csv_read, excel_read

test_data = ('''id;currency_code;amount
001;RUR;167865.71
002;USD;5466.65
003;EUR;657.54
004;RUR;56437.96
005;USD;768.94''')

expected_data = [
    {'id': '001', 'currency_code': 'RUR', 'amount': '167865.71'},
    {'id': '002', 'currency_code': 'USD', 'amount': '5466.65'},
    {'id': '003', 'currency_code': 'EUR', 'amount': '657.54'},
    {'id': '004', 'currency_code': 'RUR', 'amount': '56437.96'},
    {'id': '005', 'currency_code': 'USD', 'amount': '768.94'}
]


@patch('builtins.open')
def test_csv_read(mock_file):
    mock_file.return_value = mock_open(read_data=test_data).return_value
    result = csv_read('file_path.csv')
    assert result == expected_data
    mock_file.assert_called_once_with('file_path.csv', 'r', encoding='utf-8')


@patch('builtins.open')
def test_csv_read_empty_file(mock_file):
    mock_file.return_value = mock_open(read_data='').return_value
    result = csv_read('empty.csv')
    assert result == []
    mock_file.assert_called_once_with('empty.csv', 'r', encoding='utf-8')


test_df = pd.DataFrame({
    'id': ['001', '002', '003', '004', '005'],
    'currency_code': ['RUR', 'USD', 'EUR', 'RUR', 'USD'],
    'amount': [167865.71, 5466.65, 657.54, 56437.96, 768.94]
})


@patch('pandas.read_excel')
def test_excel_read(mock):
    mock.return_value = test_df
    result = excel_read('path')
    expected_result = test_df.to_dict('records')
    assert result == expected_result
    mock.assert_called_once()
