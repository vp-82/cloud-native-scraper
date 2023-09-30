"""
Tests for the state adapter module.
"""

import pytest
# import pytest
# from simple_url_collector import SimpleURLCollector
from state_adapter import GCPStateAdapter, LocalFileStateAdapter
from state_adapter_factory import StateAdapterFactory

from app_config.scraper_config import ScraperConfig

TEST_STATE_FILE = "tests/url_collector/unit/state.json"


@pytest.fixture(scope="module")
def config():
    """ Fixture for the ScraperConfig object. """
    return ScraperConfig()


def test_state_adapter_factory():
    """
    Test the StateAdapterFactory class.
    """

    # Test the LocalFileStateAdapter
    factory = StateAdapterFactory(config)
    state_adapter = factory.create(adapter_type='local', file_path=TEST_STATE_FILE)

    assert isinstance(state_adapter, LocalFileStateAdapter)

    # Test the GCPStateAdapter
    factory = StateAdapterFactory(config)
    state_adapter = factory.create(
        adapter_type='gcp',
        bucket_name='test-bucket',
        blob_name='blob-name')
    assert isinstance(state_adapter, GCPStateAdapter)
