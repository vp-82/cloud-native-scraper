""" State adapter module. """
import json
import logging
import os
from abc import ABC, abstractmethod

from google.cloud import firestore_v1, storage

logger = logging.getLogger(__name__)


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

        log_payload = {
            "message": "State saved to local file",
            "file_path": self.file_path
        }
        logger.info(log_payload)

    def load_state(self):
        """ Loads the state of the collector."""
        state = {}
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='UTF-8') as file:
                state = json.load(file)

        log_payload = {
            "message": "State loaded from local file",
            "file_path": self.file_path
        }
        logger.info(log_payload)

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
    """ Adapter for saving/loading state from Google Cloud Firestore."""
    def __init__(self, collection_name, document_name, **kwargs):
        self.collection_name = collection_name
        self.document_name = document_name
        self.extra_config = kwargs  # Store additional config if needed

        # Extracting configurations for Firestore Client
        credentials_path = kwargs.get('credentials_path', None)
        project_id = kwargs.get('project_id', None)

        # Set up the Firestore client
        self.firestore_db = (
            firestore_v1.Client.from_service_account_json(credentials_path)
            if credentials_path
            else firestore_v1.Client(project=project_id)
        )

    def save_state(self, state):
        doc_ref = self.firestore_db.collection(self.collection_name).document(self.document_name)
        doc_ref.set(state)

        log_payload = {
            "message": "State saved to Firestore",
            "collection_name": self.collection_name,
            "document_name": self.document_name
        }
        logger.info(log_payload)

    def load_state(self):
        doc_ref = self.firestore_db.collection(self.collection_name).document(self.document_name)
        doc = doc_ref.get()

        log_payload = {
            "message": "State loaded from Firestore",
            "collection_name": self.collection_name,
            "document_name": self.document_name
        }
        logger.info(log_payload)

        if doc.exists:
            return doc.to_dict()
        return {}
