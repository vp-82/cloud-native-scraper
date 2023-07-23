"""
Simple URL collector.
"""

import logging

from base_url_collector import BaseURLCollector


class SimpleURLCollector(BaseURLCollector):
    """
    Simple URL collector.
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def load_state(self):
        """ Loads the state of the collector. """

    def save_state(self):
        """ Saves the state of the collector. """

    def collect(self):
        """ Collects the base URLs from the given source. """
        all_urls = []
        for base_url in self.urls:
            if base_url in self.state:
                continue

            response = requests.get(base_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            urls_from_page = self.extract_urls(soup)

            # Filter URLs to only include those that start with the base_url
            urls_from_page = [url for url in urls_from_page if url.startswith(base_url)]
            
            all_urls.extend(urls_from_page)

            self.state[base_url] = True
            self.save_state()
            self.publisher_adapter.publish(base_url)

        return all_urls
