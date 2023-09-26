from abc import ABC, abstractmethod


class URLFilterPlugin(ABC):

    @abstractmethod
    def should_collect(self, url: str) -> bool:
        """Determine if the URL should be collected."""
        pass
