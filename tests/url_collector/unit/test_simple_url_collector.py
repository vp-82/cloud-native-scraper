"""
Tests for the SimpleUrlCollector class.
"""

# import pytest

from src.url_collector.simple_url_collector import SimpleURLCollector


def test_constructor():
    """
    Test the constructor of the SimpleUrlCollector class.
    """
    _ = SimpleURLCollector(urls=['https://www.google.com/'])
