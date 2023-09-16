"""
Tests for the BaseUrlCollector class.
"""

import pytest

from src.url_collector.base_url_collector import BaseURLCollector


def test_constructor():
    """
    Test the constructor of the BaseUrlCollector class.
    """
    with pytest.raises(TypeError):

        _ = BaseURLCollector(  # type: ignore # pylint: disable=abstract-class-instantiated
            base_urls=['https://google.com'],
            start_urls=['https://google.com/test']
            )
