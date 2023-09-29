""" Publisher Adapter """
from abc import ABC, abstractmethod
from typing import Optional

from google.cloud import pubsub_v1


class AbstractPublisherAdapter(ABC):
    """ Abstract Publisher Adapter """
    @abstractmethod
    def publish(self, message: str):
        """ Publishes a message """
        pass  # pylint: disable=unnecessary-pass


class GCPPubSubPublisherAdapter(AbstractPublisherAdapter):
    """ GCP Pub/Sub Publisher Adapter """
    def __init__(self, project_id: str, topic_name: str, credentials_path: Optional[str]):
        if credentials_path:
            self.publisher = pubsub_v1.PublisherClient.from_service_account_json(credentials_path)
        else:
            self.publisher = pubsub_v1.PublisherClient()

        self.topic_path = self.publisher.topic_path(project_id, topic_name)

    def publish(self, message: str):
        """Publish a message to GCP Pub/Sub."""
        self.publisher.publish(self.topic_path, data=message.encode('utf-8'))
