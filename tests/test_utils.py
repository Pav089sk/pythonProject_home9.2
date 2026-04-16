from unittest.mock import patch
from src.utils import transaction_data

@patch('operations')
def test_transaction_data(mock_data):
    mock_data.return_value = [{"key": "value"}]
    assert transaction_data('operation') == [{"key": "value"}]
    mock_data.assert_called()