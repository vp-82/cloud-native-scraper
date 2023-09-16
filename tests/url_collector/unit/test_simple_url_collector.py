"""
Tests for the SimpleUrlCollector class.
"""

from unittest.mock import patch

import pytest
from html_responses import BASEURL_RESPONSE

from src.url_collector.simple_url_collector import SimpleURLCollector

BASE_URL = "https://www.dwd.de/SiteGlobals/Forms/ThemaDesTages"
START_URL = "https://www.dwd.de/SiteGlobals/Forms/ThemaDesTages/ThemaDesTages_Formular.html"


@pytest.fixture(name='base_url_rsponse')
def fixture_base_url_response():
    """ Fixture for the base URL response."""
    return BASEURL_RESPONSE


def test_constructor():
    """
    Test the constructor of the SimpleUrlCollector class.
    """
    _ = SimpleURLCollector(base_urls=[BASE_URL], start_urls=[START_URL])


@patch('src.url_collector.simple_url_collector.requests.get')
def test_collect(base_url_response):
    """ Test the collect method of the SimpleUrlCollector class. """
    with patch('src.url_collector.simple_url_collector.requests.get') as mock_get:
        mock_get.return_value = base_url_response
        collector = SimpleURLCollector(base_urls=[BASE_URL], start_urls=[START_URL])
        urls = collector.collect()
        assert len(urls) == 1
        assert urls[0] == START_URL
