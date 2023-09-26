import json

import pkg_resources


class PluginManager:

    def __init__(self, config_file="config.json"):
        with open(config_file, 'r') as f:
            self.config = json.load(f)
        self.url_filter_plugin = self._load_plugin("url_filter")

    def _load_plugin(self, plugin_type):
        plugin_name = self.config.get("active_plugins", {}).get(plugin_type)
        if not plugin_name:
            return None
        for entry_point in pkg_resources.iter_entry_points(f'scraper_plugins.{plugin_type}'):
            if entry_point.name == plugin_name:
                return entry_point.load()()
        return None
