import pytest
from unittest.mock import patch
import sys
sys.path.append('..')
from processor import fetch_multiple_batches


@patch('processor.fetch_all_data')
def test_generator_yields_correct_count(mock_fetch):
    # Mock what fetch_all_data returns
    mock_fetch.return_value = [
        {'results': [{'name': {'first': 'John'}}]},
        {'value': 'joke'}
    ]
    
    # Get all batches from generator
    batches = list(fetch_multiple_batches(3))
    
    # Assertions
    assert len(batches) == 3
    assert mock_fetch.call_count == 3  # Called 3 times