"""
Abstract state adapter.
"""
from abc import ABC, abstractmethod


class AbstractStateAdapter(ABC):
    """ Abstract state adapter. """

    @abstractmethod
    def save_state(self, state):
        """ Saves the state of the collector."""

    @abstractmethod
    def load_state(self):
        """ Loads the state of the collector."""
