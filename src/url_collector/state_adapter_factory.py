""" Factory for creating state adapters."""

from firestore_state_adapter import FirestoreStateAdapter
from gcp_state_adapter import GCPStateAdapter
from local_state_adapter import LocalFileStateAdapter


class StateAdapterFactory:
    """ Factory for creating state adapters. """

    @staticmethod
    def create(adapter_type, **kwargs):
        """ Creates a state adapter. """
        if adapter_type == 'local':
            return LocalFileStateAdapter(kwargs.get('file_path', 'state.json'))
        elif adapter_type == 'gcp':
            return GCPStateAdapter(kwargs['bucket_name'], kwargs['blob_name'])
        elif adapter_type == 'firestore':
            return FirestoreStateAdapter(kwargs['collection_name'], kwargs['document_name'])
        else:
            raise ValueError(f"Unsupported adapter type: {adapter_type}")
