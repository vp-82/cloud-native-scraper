"""
Simple URL collector.
"""

import logging
from typing import List

import requests
from base_url_collector import BaseURLCollector
from bs4 import BeautifulSoup


class SimpleURLCollector(BaseURLCollector):
    """
    Simple URL collector.
    """
    def __init__(self, urls: List[str]):
        super().__init__(urls)
        self.logger = logging.getLogger(__name__)
        self.state = {}

    def load_state(self):
        """ Loads the state of the collector. """

    def save_state(self):
        """ Saves the state of the collector. """

    def collect(self) -> List[str]:
        """ Collects the base URLs from the given source. """
        all_urls = []
        for base_url in self.urls:
            if base_url in self.state:
                continue

            response = requests.get(base_url, timeout=20)
            soup = BeautifulSoup(response.text, 'html.parser')
            urls_from_page = self.extract_urls(soup)

            # Filter URLs to only include those that start with the base_url
            urls_from_page = [url for url in urls_from_page if url.startswith(base_url)]

            all_urls.extend(urls_from_page)

            self.state[base_url] = True
            self.save_state()
            # self.publisher_adapter.publish(base_url)

        return all_urls

    def extract_urls(self, soup: BeautifulSoup) -> List[str]:
        """ Extracts URLs from the given soup. """
        urls = []
        for link in soup.find_all('a'):
            urls.append(link.get('href'))
        return urls
