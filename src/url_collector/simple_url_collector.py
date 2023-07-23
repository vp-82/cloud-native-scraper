"""
Simple URL collector.
"""

import logging

from base_url_collector import BaseURLCollector


class SimpleURLCollector(BaseURLCollector):
    """
    Simple URL collector.
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def load_state(self):
        """ Loads the state of the collector. """

    def save_state(self):
        """ Saves the state of the collector. """

    def collect(self):
        """ Collects the base URLs from the given source. """
