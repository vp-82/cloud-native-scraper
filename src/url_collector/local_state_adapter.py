"""
Adapter for saving/loading state from a local file.
"""
import json
import os

from .abstract_state_adapter import AbstractStateAdapter


class LocalFileStateAdapter(AbstractStateAdapter):
    """ Adapter for saving/loading state from a local file. """

    def __init__(self, file_path='state.json'):
        self.file_path = file_path

    def save_state(self, state):
        """ Saves the state of the collector."""
        with open(self.file_path, 'w', encoding='UTF-8') as file:
            json.dump(state, file)

    def load_state(self):
        """ Loads the state of the collector."""
        state = {}
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='UTF-8') as file:
                state = json.load(file)
        return state
