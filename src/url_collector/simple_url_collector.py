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

from plugin_manager import PluginManager

logger = logging.getLogger(__name__)


class SimpleURLCollector(BaseURLCollector):
    """
    Simple URL collector.
    """
    def __init__(self, base_urls: List[str],
                 start_urls: List[str],
                 state_adapter: AbstractStateAdapter):
        super().__init__(base_urls=base_urls, start_urls=start_urls)
        self.state_adapter = state_adapter
        self.plugin_manager = PluginManager()
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

        log_payload = {
            "message": "State loaded",
            "visited_urls_count": len(self.visited_urls),
            "pending_urls_count": len(self.pending_urls),
            "errors_count": len(self.errors)
        }
        logger.info(log_payload)

    def save_state(self):
        """ Saves the state of the collector. """
        state = {
            'pending_urls': list(self.pending_urls),  # Convert deque to list for serialization
            'errors': self.errors,
            'visited_urls': list(self.visited_urls),  # Convert set to list for serialization
        }
        self.state_adapter.save_state(state)

        log_payload = {
            "message": "State saved",
            "visited_urls_count": len(self.visited_urls),
            "pending_urls_count": len(self.pending_urls),
            "errors_count": len(self.errors)
        }
        logger.info(log_payload)

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

                log_payload = {
                    "message": "Requesting URL",
                    "url": start_url
                }
                logger.debug(log_payload)

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
                    log_payload = {
                        "message": "Extracting URLs from page",
                        "url": start_url
                    }
                    logger.debug(log_payload)

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

                log_payload = {
                    "message": "URL added to visited",
                    "visited_url": start_url
                }
                logger.info(log_payload)

        except Exception as ex:
            # If an error occurs, save the current state
            logger.error(f"Error occurred during scraping: {ex}")
            self.errors.append(str(ex))
            self.pending_urls = list(pending_urls)
            self.save_state()
            raise ex  # Re-raise the exception after saving the state
        return list(self.visited_urls)

    def extract_urls(self, soup: BeautifulSoup, base_url: str) -> List[str]:
        """ Extracts URLs from the given soup and converts them to absolute URLs. """
        urls = []
        for link in soup.find_all('a'):
            href = link.get('href')

            # After extracting a URL, use the filter plugin to decide whether to process it
            url_filter_plugin = self.plugin_manager.url_filter_plugin
            if url_filter_plugin and not url_filter_plugin.should_collect(href):
                continue

            # Skip if href is None
            if not href or "#" in href:
                continue

            href = href.split(';jsessionid=')[0]
            absolute_url = urljoin(base_url, href)
            urls.append(absolute_url)

            log_payload = {
                "message": "URLs extracted from page",
                "url": absolute_url,
                "extracted_urls_count": len(urls)
            }
            logger.debug(log_payload)

        return urls

    def __enter__(self):
        return self

    # Save the state when exiting the context only if an exception has not occurred
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
