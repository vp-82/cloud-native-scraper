"""
Tests for the SimpleUrlCollector class.
"""

import json
import os
from unittest.mock import Mock, patch

import pytest
from html_responses import BASEURL_RESPONSE
from simple_url_collector import SimpleURLCollector
from state_adapter import AbstractStateAdapter
from state_adapter_factory import StateAdapterFactory

BASE_URL = "https://www.dwd.de/"
START_URL = "https://www.dwd.de/DE/service/impressum/impressum_node.html"


@pytest.fixture(name='base_url_rsponse')
def fixture_base_url_response():
    """ Fixture for the base URL response."""
    return BASEURL_RESPONSE


def test_constructor():
    """
    Test the constructor of the SimpleUrlCollector class.
    """
    mock_state_adapter = Mock(spec=AbstractStateAdapter)
    _ = SimpleURLCollector(base_urls=[BASE_URL], start_urls=[START_URL], state_adapter=mock_state_adapter)


def test_collect():
    """ Test the collect method of the SimpleUrlCollector class. """
    with patch('src.url_collector.simple_url_collector.requests.get',
               return_value=Mock(text=BASEURL_RESPONSE)) as _:

        # Mock the state adapter
        mock_state_adapter = Mock(spec=AbstractStateAdapter)
        mock_state_adapter.save_state.return_value = None  # Mocked save_state to do nothing

        with SimpleURLCollector(base_urls=[BASE_URL],
                                start_urls=[START_URL],
                                state_adapter=mock_state_adapter) as collector:
            urls = collector.collect()
        assert len(urls) == 55
        # assert urls[0] == START_URL


def test_collect_with_exception():
    """ Test the collect method of the SimpleUrlCollector class when an exception occurs. """
    with patch('src.url_collector.simple_url_collector.requests.get',
               side_effect=Exception("HTTP Exception")) as _:  # Mock the requests.get method

        # Mock the state adapter
        mock_state_adapter = Mock(spec=AbstractStateAdapter)
        mock_state_adapter.save_state.return_value = None  # Mocked save_state to do nothing

        with SimpleURLCollector(base_urls=[BASE_URL],
                                start_urls=[START_URL],
                                state_adapter=mock_state_adapter) as collector:
            with pytest.raises(Exception):
                _ = collector.collect()

        # Assert that the state was saved
        assert mock_state_adapter.save_state.call_count == 1


def test_collect_with_exception_and_state():
    """ Test the collect method of the SimpleUrlCollector class when an exception occurs and state is available. """
    with patch('src.url_collector.simple_url_collector.requests.get',
               side_effect=Exception("HTTP Exception")) as _:  # Mock the requests.get method

        state_adapter = StateAdapterFactory.create(adapter_type='local',
                                                   file_path='tests/url_collector/unit/state.json')

        with SimpleURLCollector(base_urls=[BASE_URL],
                                start_urls=[START_URL],
                                state_adapter=state_adapter) as collector:

            with pytest.raises(Exception):
                _ = collector.collect()

    assert os.path.exists("tests/url_collector/unit/state.json") is True
    # Read and load the JSON file content
    with open('tests/url_collector/unit/state.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)

    # Assert the content
    assert data['pending_urls'] == []
    assert data['errors'] == ["HTTP Exception"]
    assert data['visited_urls'] == []

    os.remove('tests/url_collector/unit/state.json')
