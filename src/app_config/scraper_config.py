import json
import logging
import os


def detect_gcp():
    """Detect if we're running on GCP."""
    return os.environ.get('GAE_INSTANCE') is not None

def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Formatter for local logging
    local_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')

    # Formatter for GCP structured logging
    class GCPJSONFormatter(logging.Formatter):
        def format(self, record):
            log_dict = {
                "severity": record.levelname,
                "logger": record.name,
                "message": record.getMessage()
            }
            return json.dumps(log_dict)

    gcp_formatter = GCPJSONFormatter()

    if detect_gcp():
        # GCP logging configuration
        gcp_handler = logging.StreamHandler()
        gcp_handler.setFormatter(gcp_formatter)
        logger.addHandler(gcp_handler)
    else:
        # Local logging configuration
        local_handler = logging.StreamHandler()
        local_handler.setFormatter(local_formatter)
        logger.addHandler(local_handler)

        file_handler = logging.FileHandler('app.log')
        file_handler.setFormatter(local_formatter)
        logger.addHandler(file_handler)

    return logger

# Additional configurations (like database, API keys, etc.) can be added here in the future.
