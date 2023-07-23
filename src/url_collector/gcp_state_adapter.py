"""
Adapter for saving/loading state from Google Cloud Storage.
"""

import json

from abstract_state_adapter import AbstractStateAdapter
from google.cloud import storage


class GCPStateAdapter(AbstractStateAdapter):
    """ Adapter for saving/loading state from Google Cloud Storage. """

    def __init__(self, bucket_name, blob_name):
        self.bucket_name = bucket_name
        self.blob_name = blob_name
        self.storage_client = storage.Client()

    def save_state(self, state):
        """ Saves the state of the collector."""
        bucket = self.storage_client.bucket(self.bucket_name)
        blob = bucket.blob(self.blob_name)
        blob.upload_from_string(json.dumps(state))

    def load_state(self):
        """ Loads the state of the collector."""
        bucket = self.storage_client.bucket(self.bucket_name)
        blob = bucket.blob(self.blob_name)
        if blob.exists():
            return json.loads(blob.download_as_text())
        return {}
