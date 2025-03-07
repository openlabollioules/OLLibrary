# Utility Module

This module provides various utility functions to work with JSON and String data.

## Installation

To install the required dependencies, run:

```sh
pip install -r requirements.txt
```

## JSON Service

The JSON service provides functions to work with JSON data.

### Functions

#### `extract_json(data: any) -> dict`

Extract and return a JSON object from the given input `data`.

- **Parameters:**
  - `data` (any): The input data to extract JSON from. Can be a dict, list, or str.
- **Returns:**
  - `dict` or `list`: A parsed JSON object (usually a dict or list).
- **Raises:**
  - `ValueError`: If no valid JSON can be extracted from the input.

## Text Service

The Text service provides functions to work with String data.

### Functions

#### `remove_tags_no_keep(text: str, start: str) -> str`

Remove all text between two tags (`start` and `end`), tags included.

- **Parameters:**
  - `text` (str): Text to remove tags from.
  - `start` (str): Starting tag.
  - `end` (str): Ending tag.
- **Returns:**
  - `str`: Text with tags removed.

#### `remove_tags_keep(text: str, start: str, end: str) -> str`

Remove the tags and keep the text between them.

- **Parameters:**
  - `text` (str): Text to remove tags from.
  - `start` (str): Starting tag.
  - `end` (str): Ending tag.
- **Returns:**
  - `str`: Text with tags removed.

## Configuration Manager

The Configuration Manager module provides functionality to manage application configuration through a JSON file system.

### Class

#### `Config`

Manages application configuration through a JSON file system. Provides functionality to load, save, and manipulate configuration settings persistently.

- **Attributes:**
  - `config_file` (str): Full path to the JSON configuration file.
  - `config` (dict): Dictionary containing the current configuration settings.

- **Methods:**
  - `__init__(config_dir: str = None)`: Initialize a Config instance.
  - `load_config()`: Load configuration from a JSON file.
  - `save_config()`: Save the current configuration to a JSON file.
  - `get(key, default=None)`: Retrieve a configuration value by key.
  - `set(key, value)`: Set a configuration value and save the configuration.
  - `show_config()`: Return a formatted JSON string of the current configuration.