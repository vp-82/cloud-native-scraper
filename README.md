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

`git clone https://github.com/vp-82/cloud-native-scraper.git`
`cd repo/services/url_collector`

For detailed instructions on how to run and deploy each service, see the README files in the respective service directories.

## Testing

Each service directory contains a `tests` folder with tests for that service. For instructions on how to run these tests, see the README files in the respective service directories.

## Linting and Formatting

We use flake8 for Python linting, and golangci-lint for Go. Formatting rules are defined in the `.formatter.cfg` files in each service directory. Check these files for the specific rules we follow.

## Deploying

We use GitHub Actions for CI/CD. Workflows are defined under the `.github/workflows` directory. These workflows automatically test, build, and deploy our services whenever changes are pushed to the repository.

## Contributing

If you wish to contribute to the project, please see the `CONTRIBUTING.md` file for guidelines.

## License

This project is licensed under the MIT License.

