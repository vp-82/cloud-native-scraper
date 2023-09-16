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
    def __init__(self, base_urls: List[str], start_urls: List[str]):
        super().__init__(base_urls=base_urls, start_urls=start_urls)
        self.logger = logging.getLogger(__name__)
        self.state = {}

    def load_state(self):
        """ Loads the state of the collector. """

    def save_state(self):
        """ Saves the state of the collector. """

    def collect(self) -> List[str]:
        """ Collects the base URLs from the given source. """
        all_urls = []
        for start_url in self.start_urls:

            response = requests.get(start_url, timeout=20)
            soup = BeautifulSoup(response.text, 'html.parser')
            urls_from_page = self.extract_urls(soup)

            # Filter URLs to only include those that start with the base_url
            urls_from_page = [url for url in urls_from_page if any(
                url.startswith(base_url) for base_url in self.base_urls)]

            all_urls.extend(urls_from_page)

            self.save_state()
            # self.publisher_adapter.publish(base_url)

        return all_urls

    def extract_urls(self, soup: BeautifulSoup) -> List[str]:
        """ Extracts URLs from the given soup. """
        urls = []
        for link in soup.find_all('a'):
            urls.append(link.get('href'))
        return urls
