import logging

from scraper_config import configure_logging
from simple_url_collector import SimpleURLCollector
from state_adapter_factory import StateAdapterFactory

# Set up the logging configuration
configure_logging()

# Logger instance for this main module
logger = logging.getLogger(__name__)

def run_scraper():
    # Assuming SimpleURLCollector is the entry point for the scraper
    try:

        state_adapter = StateAdapterFactory.create(adapter_type='local',
                                                   file_path='state.json')

        collector = SimpleURLCollector(state_adapter=state_adapter, base_urls=['https://www.example.com'], start_urls=['https://www.example.com'])
        collected_urls = collector.collect()
        logger.info(f"Scraper finished. Collected {len(collected_urls)} URLs.")
    except Exception as e:
        logger.error(f"Error while running the scraper: {e}")

if __name__ == "__main__":
    logger.info("Starting the scraper...")
    run_scraper()
