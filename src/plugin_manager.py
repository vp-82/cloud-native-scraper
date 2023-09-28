import json

import pkg_resources


class PluginManager:

    @staticmethod
    def load_active_plugins():
        # Load the configuration directly within the method
        with open("config.json", "r") as f:
            config = json.load(f)

        active_filter_plugins = []
        active_transform_plugins = []

        # Load and instantiate filter plugins
        for entry_point in pkg_resources.iter_entry_points('scraper_plugins.url_filter'):
            if entry_point.name in config["url_filters"]:
                filter_plugin_class = entry_point.load()
                active_filter_plugins.append(filter_plugin_class())

        # Load and instantiate transformer plugins
        for entry_point in pkg_resources.iter_entry_points('scraper_plugins.url_transformer'):
            if entry_point.name in config["url_transformers"]:
                transform_plugin_class = entry_point.load()
                active_transform_plugins.append(transform_plugin_class())

        return active_filter_plugins, active_transform_plugins
