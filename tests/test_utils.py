import json
from unittest.mock import Mock, mock_open, patch

from src.utils import transaction_data


@patch("json.load")
def test_transaction_data(mock_data):
    """Тест функция если в JSON файле корректный список"""
    mock_data.return_value = [{"id": 1, "amount": 100}]
    with patch("builtins.open"):
        result = transaction_data("test.json")
    assert result == [{"id": 1, "amount": 100}]
    mock_data.assert_called_once()


@patch("json.load")
def test_not_list(mock_data_list):
    """Тест функция если в JSON файле не список"""
    mock_data_list.return_value = {"id": 1, "amount": 100}
    with patch("builtins.open", mock_open(read_data="test")):
        result = transaction_data("test2.json")
    assert result == []
    mock_data_list.assert_called_once()


def test_file_not_found():
    """Тест: обработка отсутствующего файла (FileNotFoundError)"""
    with patch("builtins.open", side_effect=FileNotFoundError) as open_error:
        result = transaction_data("not_found.json")
        assert result == []
    open_error.assert_called_once_with("not_found.json")


def test_invalid_json():
    """Тест: обработка некорректного JSON (JSONDecodeError)"""
    with patch("builtins.open") as invalid_json:
        with patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0)):
            result = transaction_data("invalid.json")
        assert result == []
    invalid_json.assert_called_once_with("invalid.json")
