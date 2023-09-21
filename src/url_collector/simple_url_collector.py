"""
Simple URL collector.
"""
import logging
from collections import deque
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
                 state_adapter: AbstractStateAdapter):
        super().__init__(base_urls=base_urls, start_urls=start_urls)
        self.logger = logging.getLogger(__name__)
        self.state_adapter = state_adapter
        self.visited_urls = set()
        self.pending_urls = []
        self.errors = []
        # Load the state on initialization
        self.load_state()

    def load_state(self):
        """ Loads the state of the collector. """
        self.state = self.state_adapter.load_state() or {}
        self.visited_urls = set(self.state.get('visited_urls', []))
        self.pending_urls = deque(self.state.get('pending_urls', []))

    def save_state(self):
        """ Saves the state of the collector. """
        state = {
            'pending_urls': list(self.pending_urls),  # Convert deque to list for serialization
            'errors': self.errors,
            'visited_urls': list(self.visited_urls),  # Convert set to list for serialization
        }
        self.state_adapter.save_state(state)
        self.logger.info(f"State saved with current state: {self.state}")

    def collect(self) -> List[str]:
        """ Collects the base URLs from the given source. """

        if not self.pending_urls:
            pending_urls = deque(self.start_urls)  # Use a queue to manage pending URLs
        else:
            pending_urls = deque(self.pending_urls)  # Use a queue to manage pending URLs

        try:
            while pending_urls:  # Continue scraping as long as there are pending URLs

                start_url = pending_urls.popleft()  # Get the next URL to scrape

                # Skip if the URL has already been visited
                if start_url in self.visited_urls:
                    continue

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

                    # Add URLs from the page to the pending list if they haven't been visited
                    for url in urls_from_page:
                        if url not in self.visited_urls:
                            pending_urls.append(url)

                # Add the start_url to the visited_urls set
                self.visited_urls.add(start_url)

        except Exception as ex:
            # If an error occurs, save the current state
            self.logger.error(f"Error occurred during scraping: {ex}")
            self.errors.append(str(ex))
            self.pending_urls = list(pending_urls)
            raise  # Re-raise the exception after saving the state
        return list(self.visited_urls)

    def extract_urls(self, soup: BeautifulSoup, base_url: str) -> List[str]:
        """ Extracts URLs from the given soup and converts them to absolute URLs. """
        urls = []
        for link in soup.find_all('a'):
            href = link.get('href')

            # Skip if href is None
            if not href or "#" in href:
                continue

            href = href.split(';jsessionid=')[0]
            absolute_url = urljoin(base_url, href)
            urls.append(absolute_url)
        return urls

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save_state()
