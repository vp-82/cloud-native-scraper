"""Factory for creating publisher adapters"""
from publisher_adapter import GCPPubSubPublisherAdapter, LocalPublisherAdapter


class PublisherAdapterFactory:
    """Factory for creating publisher adapters"""
    def __init__(self, config):
        self.config = config

    def create(self, publisher_type):
        """Creates a publisher adapter."""
        if publisher_type == 'GCPPubSub':
            return GCPPubSubPublisherAdapter(
                project_id=self.config['gcp']['project_id'],
                topic_name=self.config['gcp']['pubsub_topic'],
                credentials_path=self.config['gcp']['credentials_path']
            )
        elif publisher_type == 'LocalPublisher':
            return LocalPublisherAdapter()
        else:
            raise ValueError(f"Unknown publisher type: {publisher_type}")
