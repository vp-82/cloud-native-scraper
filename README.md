# cloud-native-scraper
A web scraper that runs in the cloud

# Web Scraping Microservices

This project contains a set of microservices built in Python and Go for web scraping purposes. The project includes services for URL collection, web scraping, and content processing. The infrastructure for these services is managed using Terraform.

## Structure of the Repository

The project is organized into several directories:

- `services`: This directory contains the source code for the microservices.
  - `url_collector`: This service, written in Python, collects URLs for the scraper service. It includes various URL collectors under `url_collectors` that can be customized as needed.
  - `scraper`: This service, written in Go, scrapes data from websites given URLs from the `url_collector` service. It includes various scrapers under `scrapers` that can be customized as needed.
  - `content_processor`: This service, written in Python, processes the scraped data and applies language models to extract insights.
- `terraform`: This directory contains the Terraform configuration for managing the infrastructure.

## Getting Started

To get started with the project, clone the repository and navigate to the desired service:

```bash
git clone https://github.com/username/repo.git
cd repo/services/url_collector
