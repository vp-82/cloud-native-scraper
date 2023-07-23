"""
Base URL Collector.
"""
from abc import ABC, abstractmethod


class BaseURLCollector(ABC):
    """ Base URL Collector"""

    def __init__(self, urls):
        self.urls = urls

    @abstractmethod
    def collect(self):
        """ Collects the base URLs from the given source. """

    @abstractmethod
    def save_state(self):
        """ Saves the state of the collector. """

    @abstractmethod
    def load_state(self):
        """ Loads the state of the collector. """
