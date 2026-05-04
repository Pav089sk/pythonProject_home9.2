from unittest.mock import Mock, patch

from src.external_api import transaction_amount


@patch("requests.request")
def test_transaction_amount_success(mock_request):
    """Успешный ответ от API — функция возвращает конвертированную сумму"""
    operation = {"operationAmount": {"currency": {"code": "USD"}, "amount": 85}}
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 8500}
    mock_request.return_value = mock_response
    result = transaction_amount(operation)
    assert result == 8500
    mock_request.assert_called_once()


@patch("requests.request")
def test_transaction_amount_no_amount(mock_request):
    operation = {}
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": None}
    mock_request.return_value = mock_response
    result = transaction_amount(operation)
    assert result is None
    mock_request.assert_called_once()
