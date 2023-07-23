"""
Base URL Collector.
"""
from abc import ABC, abstractmethod
from typing import List


class BaseURLCollector(ABC):
    """ Base URL Collector"""

    def __init__(self,  urls: List[str]):
        self.urls = urls

    @abstractmethod
    def collect(self) -> List[str]:
        """ Collects the base URLs from the given source. """

    @abstractmethod
    def save_state(self):
        """ Saves the state of the collector. """

    @abstractmethod
    def load_state(self):
        """ Loads the state of the collector. """
