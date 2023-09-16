"""
Tests for the SimpleUrlCollector class.
"""

from unittest.mock import Mock, patch

import pytest
from html_responses import BASEURL_RESPONSE

from src.url_collector.simple_url_collector import SimpleURLCollector
from src.url_collector.state_adapter import AbstractStateAdapter

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

        collector = SimpleURLCollector(base_urls=[BASE_URL], start_urls=[START_URL], state_adapter=mock_state_adapter)
        urls = collector.collect()
        assert len(urls) == 98
        # assert urls[0] == START_URL
