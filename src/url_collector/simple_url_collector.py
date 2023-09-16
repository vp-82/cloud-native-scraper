"""
Simple URL collector.
"""
import logging
from typing import List
from urllib.parse import urljoin

import requests
from base_url_collector import BaseURLCollector
from bs4 import BeautifulSoup
from state_adapter import AbstractStateAdapter


class SimpleURLCollector(BaseURLCollector):
    """
    Simple URL collector.
    """
    def __init__(self, base_urls: List[str],
                 start_urls: List[str],
                 state_adapter: AbstractStateAdapter,
                 batch_size: int = 10):
        super().__init__(base_urls=base_urls, start_urls=start_urls)
        self.logger = logging.getLogger(__name__)
        self.state_adapter = state_adapter
        self.batch_size = batch_size
        self.current_batch_count = 0
        # Load the state on initialization
        self.state = self.load_state() or {}

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

            # Determine the corresponding base_url for the start_url
            corresponding_base_url = None
            for base_url in self.base_urls:
                if start_url.startswith(base_url):
                    corresponding_base_url = base_url
                    break

            # If a corresponding base URL is found, extract URLs
            if corresponding_base_url:
                urls_from_page = self.extract_urls(soup, corresponding_base_url)

                # Filter URLs to only include those that start with the base_url
                urls_from_page = [url for url in urls_from_page if any(
                    url.startswith(base_url) for base_url in self.base_urls)]

                all_urls.extend(urls_from_page)
                self.save_state()

        return all_urls

    def extract_urls(self, soup: BeautifulSoup, base_url: str) -> List[str]:
        """ Extracts URLs from the given soup and converts them to absolute URLs. """
        urls = []
        for link in soup.find_all('a'):
            href = link.get('href')

            # Skip if href is None
            if not href or "#" in href:
                continue

            absolute_url = urljoin(base_url, href)
            urls.append(absolute_url)
        return urls
