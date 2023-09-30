""" Factory for creating state adapters."""

from state_adapter import (FirestoreStateAdapter, GCPStateAdapter,
                           LocalFileStateAdapter)


class StateAdapterFactory:
    """ Factory for creating state adapters. """
    def __init__(self, config):
        self.config = config

    def create(self, adapter_type, **kwargs):
        """ Creates a state adapter. """
        if adapter_type == 'local':
            return LocalFileStateAdapter(kwargs.get('file_path', 'state.json'))
        elif adapter_type == 'gcp':
            return GCPStateAdapter(kwargs['bucket_name'], kwargs['blob_name'])
        elif adapter_type == 'firestore':
            # Extracting specific config and passing them as explicit parameters
            collection_name = kwargs.get('collection_name', '')
            document_name = kwargs.get('document_name', '')

            # Here you might pass additional config from your self.config if needed
            gcp_config = self.config.get('gcp', {})
            kwargs.update(gcp_config)

            return FirestoreStateAdapter(collection_name, document_name, **kwargs)
        else:
            raise ValueError(f"Unsupported adapter type: {adapter_type}")
