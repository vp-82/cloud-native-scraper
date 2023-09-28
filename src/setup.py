from setuptools import find_packages, setup

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    entry_points={
        'scraper_plugins.url_filter': [
            'GeneralFilter = general_filter:GeneralFilter',
        ],
        'scraper_plugins.url_transformer': [
            'JSessionIDRemover = jsessionid_transformer:JSessionIDRemover',
        ],
    },
)