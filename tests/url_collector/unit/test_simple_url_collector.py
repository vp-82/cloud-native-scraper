"""
Tests for the SimpleUrlCollector class.
"""

import json
import os
import time
from unittest.mock import Mock, patch

import pytest
import requests
from html_responses import BASEURL_RESPONSE
from simple_url_collector import SimpleURLCollector
from state_adapter import AbstractStateAdapter
from state_adapter_factory import StateAdapterFactory

BASE_URL = "https://www.dwd.de/"
START_URL = "https://www.dwd.de/DE/service/impressum/impressum_node.html"
TEST_STATE_FILE = "tests/url_collector/unit/state.json"
BASE_URL_2 = "https://hamel.dev/"


@pytest.fixture(name='base_url_rsponse')
def fixture_base_url_response():
    """ Fixture for the base URL response."""
    return BASEURL_RESPONSE


# Define the fixture
@pytest.fixture
def cleanup():
    """ Fixture to clean up the state file after the test."""
    yield  # This is where your test will run
    if os.path.exists(TEST_STATE_FILE):
        os.remove(TEST_STATE_FILE)


def test_constructor():
    """
    Test the constructor of the SimpleUrlCollector class.
    """
    mock_state_adapter = Mock(spec=AbstractStateAdapter)
    mock_state_adapter.load_state.return_value = {}  # Mocked load_state to return an empty dict
    _ = SimpleURLCollector(base_urls=[BASE_URL], start_urls=[START_URL], state_adapter=mock_state_adapter)


def test_collect():
    """ Test the collect method of the SimpleUrlCollector class. """
    with patch('src.url_collector.simple_url_collector.requests.get',
               return_value=Mock(text=BASEURL_RESPONSE)) as _:

        # Mock the state adapter
        mock_state_adapter = Mock(spec=AbstractStateAdapter)
        mock_state_adapter.load_state.return_value = {}  # Mocked load_state to return an empty dict
        mock_state_adapter.save_state.return_value = None   # Mocked save_state to do nothing

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
        mock_state_adapter.load_state.return_value = {}  # Mocked load_state to return an empty dict
        mock_state_adapter.save_state.return_value = None  # Mocked save_state to do nothing

        with SimpleURLCollector(base_urls=[BASE_URL],
                                start_urls=[START_URL],
                                state_adapter=mock_state_adapter) as collector:
            with pytest.raises(Exception):
                _ = collector.collect()

        # Assert that the state was saved
        assert mock_state_adapter.save_state.call_count == 1


# Use the fixture in your test
@pytest.mark.usefixtures("cleanup")
def test_collect_with_exception_and_state():
    """ Test the collect method of the SimpleUrlCollector class when an exception occurs and state is available. """
    with patch('src.url_collector.simple_url_collector.requests.get',
               side_effect=Exception("HTTP Exception")) as _:  # Mock the requests.get method

        state_adapter = StateAdapterFactory.create(adapter_type='local',
                                                   file_path=TEST_STATE_FILE)

        with SimpleURLCollector(base_urls=[BASE_URL],
                                start_urls=[START_URL],
                                state_adapter=state_adapter) as collector:

            with pytest.raises(Exception):
                _ = collector.collect()

    assert os.path.exists(TEST_STATE_FILE) is True
    # Read and load the JSON file content
    with open(TEST_STATE_FILE, 'r', encoding='UTF-8') as file:
        data = json.load(file)

    # Assert the content
    assert data['pending_urls'] == []
    assert data['errors'] == ["HTTP Exception"]
    assert data['visited_urls'] == []


# Use the fixture in your test
@pytest.mark.usefixtures("cleanup")
def test_collect_with_error_after_20_iterations_and_resume():
    """ Test the collect method of the SimpleUrlCollector class when an error occurs after 20 iterations.
    Resume the collection after the error and stop at iteration 40."""
    # Initialize your SimpleURLCollector object here
    # collector = SimpleURLCollector(...)

    iteration_count = 0

    # Store the original requests.get method for later use
    original_requests_get = requests.get

    def mock_requests_get(*args, **kwargs):
        nonlocal iteration_count
        iteration_count += 1

        if iteration_count == 20:
            raise RuntimeError("Simulated error at iteration 20")

        if iteration_count == 40:
            raise RuntimeError("Simulated error at iteration 40")

        # Call the original requests.get method for normal behavior
        return original_requests_get(*args, **kwargs)  # pylint: disable=missing-timeout

    with patch('requests.get', side_effect=mock_requests_get):
        try:

            state_adapter = StateAdapterFactory.create(adapter_type='local',
                                                       file_path=TEST_STATE_FILE)

            with SimpleURLCollector(base_urls=[BASE_URL],
                                    start_urls=[START_URL],
                                    state_adapter=state_adapter) as collector:
                _ = collector.collect()
        except RuntimeError as ex:
            # Verify that the error is raised at iteration 20
            assert str(ex) == "Simulated error at iteration 20"

    # Verify that the state was saved
    assert os.path.exists(TEST_STATE_FILE) is True
    # Read and load the JSON file content
    with open(TEST_STATE_FILE, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        # Assert that the state was saved
        assert len(data['visited_urls']) == 19
        assert len(data['pending_urls']) > 1

    with patch('requests.get', side_effect=mock_requests_get):
        try:

            state_adapter = StateAdapterFactory.create(adapter_type='local',
                                                       file_path=TEST_STATE_FILE)

            with SimpleURLCollector(base_urls=[BASE_URL],
                                    start_urls=[START_URL],
                                    state_adapter=state_adapter) as collector:
                _ = collector.collect()
        except RuntimeError as ex:
            # Verify that the error is raised at iteration 40
            assert str(ex) == "Simulated error at iteration 40"

    # Verify that the state was saved
    assert os.path.exists(TEST_STATE_FILE) is True
    # Read and load the JSON file content
    with open(TEST_STATE_FILE, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        # Assert that the state was saved
        assert len(data['visited_urls']) == 38
        assert len(data['pending_urls']) > 1


def test_with_small_page():
    """ Test the collect method of the SimpleUrlCollector class with a small page. """
    state_adapter = StateAdapterFactory.create(adapter_type='local',
                                               file_path=TEST_STATE_FILE)

    start_time = time.perf_counter()

    with SimpleURLCollector(base_urls=[BASE_URL_2],
                            start_urls=[BASE_URL_2],
                            state_adapter=state_adapter) as collector:

        urls = collector.collect()

    end_time = time.perf_counter()

    assert len(urls) > 100
    assert end_time - start_time < 30.0
