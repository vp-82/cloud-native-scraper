""" State adapter module. """
import json
import os
from abc import ABC, abstractmethod

from google.cloud import firestore_v1, storage


class AbstractStateAdapter(ABC):
    """ Abstract state adapter. """

    @abstractmethod
    def save_state(self, state):
        """ Saves the state of the collector."""

    @abstractmethod
    def load_state(self):
        """ Loads the state of the collector."""


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


class FirestoreStateAdapter(AbstractStateAdapter):
    """ Adapter for saving/loading state from Google Cloud Firestore. """

    def __init__(self, collection_name, document_name):
        self.collection_name = collection_name
        self.document_name = document_name
        self.db = firestore_v1.Client()  # pylint: disable=invalid-name

    def save_state(self, state):
        doc_ref = self.db.collection(self.collection_name).document(self.document_name)
        doc_ref.set(state)

    def load_state(self):
        doc_ref = self.db.collection(self.collection_name).document(self.document_name)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        return {}
