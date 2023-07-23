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

        _ = BaseURLCollector(urls=['https://google.com'])  # type: ignore # pylint: disable=abstract-class-instantiated
