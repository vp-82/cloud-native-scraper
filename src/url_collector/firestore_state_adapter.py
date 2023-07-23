"""
Adapter for saving/loading state from Google Cloud Firestore.
"""

from abstract_state_adapter import AbstractStateAdapter
from google.cloud import firestore_v1


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
