# Plugin System Guide

This guide explains how to extend the capabilities of the scraper through the plugin system.

## Table of Contents

- [Plugin Basics](#plugin-basics)
- [Why Plugins?](#why-plugins)
- [Entry Points](#entry-points)
- [Plugin Setup](#plugin-setup)
- [Workflow](#workflow)
- [Benefits in Context](#benefits-in-context)
- [Adding a New Plugin](#adding-a-new-plugin)
- [Adding a New Entry Point](#adding-a-new-entry-point)

---

## Plugin Basics

In software design, a plugin is a piece of software that adds a specific feature to an existing application. By using plugins, an application can be extended in its capabilities without having to modify its core structure.

## Why Plugins?

- **Modularity**: Allows breaking down complex systems into simpler, interchangeable components.
- **Extensibility**: New features or behaviors can be added without changing the main codebase.
- **Maintainability**: It's easier to update or fix individual plugins without affecting others.

## Entry Points

To enable dynamic loading of plugins, we use "entry points". This is a feature provided by `setuptools`, a Python library for packaging. An entry point is essentially a named pointer to a function or class. Other code can then look up these pointers dynamically (at runtime) and use the functions or classes they point to.

### Code Example:

```python
entry_points={
    'scraper_plugins.url_filter': [
        'GeneralFilter = general_filter:GeneralFilter',
    ],
    ...
},
```

---

## Plugin Setup

### Plugin Interfaces

Guidelines or contracts that all corresponding plugins must follow.

### Code Example:

```python
class URLFilterPlugin:
    def should_collect(self, url: str) -> bool:
        raise NotImplementedError
```

---

### Plugin Implementations

Actual plugins that implement these interfaces.

### Code Example:

```python
class GeneralFilter(URLFilterPlugin):
    def should_collect(self, url: str) -> bool:
        return "disallowed" not in url
```

---

### Registration

Plugins are registered in the `setup.py` file using entry points, making them discoverable.

### Code Example:

```python
entry_points={
    'scraper_plugins.url_filter': [
        'GeneralFilter = general_filter:GeneralFilter',
    ],
    ...
},
```

---

### Configuration

Specify which plugins are active in `config.json`.

### Code Example:

```json
{
    "url_filters": ["GeneralFilter"],
    ...
}
```

---

### Loading Plugins

`PluginManager` reads the `config.json`, discovers registered plugins via entry points, and loads the active ones.

### Code Example:

```python
def load_active_plugins():
    with open("config.json", "r") as f:
        config = json.load(f)

    active_filter_plugins = []
    for entry_point in pkg_resources.iter_entry_points('scraper_plugins.url_filter'):
        if entry_point.name in config["url_filters"]:
            filter_plugin_class = entry_point.load()
            active_filter_plugins.append(filter_plugin_class())
```

---