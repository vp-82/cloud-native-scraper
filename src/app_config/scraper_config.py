import json
import logging
import os


class ScraperConfig:

    def __init__(self, config_file_path: str = 'config.json'):
        self.config = self.load_config(config_file_path)
        self.run_location = self.determine_run_location()
        self.setup_logging()

    def load_config(self, config_file_path: str) -> dict:
        """Load configuration from a JSON file."""
        with open(config_file_path, 'r') as file:
            return json.load(file)

    def determine_run_location(self) -> str:
        """Determine if running on GCP or locally."""
        # Using GCP_PROJECT_ID as an indicator for GCP environment
        if os.environ.get('GCP_PROJECT_ID'):
            return 'gcp'
        else:
            return 'local'

    def setup_logging(self):
        """Set up logging based on run location."""
        logging_level = self.config['logging']['level']
        if self.run_location == 'gcp':
            # Structured logging for GCP (e.g., for Google Cloud Logging)
            GCP_LOG_FORMAT = '{"severity": "%(levelname)s", "message": "%(message)s", "name": "%(name)s"}'
            logging.basicConfig(level=logging.getLevelName(logging_level), format=GCP_LOG_FORMAT)
        else:
            # Human-readable logging for local development
            LOCAL_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            logging.basicConfig(level=logging.getLevelName(logging_level), format=LOCAL_LOG_FORMAT)


# If you want to initialize the config upon import, you can instantiate it here:
# config = ScraperConfig()
# This will make the config available to all modules that import it.