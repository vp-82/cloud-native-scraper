"""
Tests for the state adapter module.
"""

# import pytest
# from simple_url_collector import SimpleURLCollector
from state_adapter import GCPStateAdapter, LocalFileStateAdapter
from state_adapter_factory import StateAdapterFactory


def test_state_adapter_factory():
    """
    Test the StateAdapterFactory class.
    """

    # Test the LocalFileStateAdapter
    state_adapter = StateAdapterFactory.create(
        adapter_type='local',
        file_path='state.json')

    assert isinstance(state_adapter, LocalFileStateAdapter)

    # Test the GCPStateAdapter
    state_adapter = StateAdapterFactory.create(
        adapter_type='gcp',
        bucket_name='test-bucket',
        blob_name='blob-name')
    assert isinstance(state_adapter, GCPStateAdapter)
