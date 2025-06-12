# Utility Module

This module provides various utility functions to work with JSON, String data, and logging.

## Installation

To install the required dependencies, run:

```sh
pip install -r requirements.txt
```

## JSON Service

The JSON service provides functions to work with JSON data.

### Functions

#### `extract_json(data: any) -> dict`

Extract and return a JSON object from the given input `data`. This function uses multiple methods to extract JSON:
1. Direct parsing if the input is already a dict or list
2. Full string parsing if the input is a pure JSON string
3. Regex-based extraction for finding JSON-like patterns
4. JSONDecoder-based extraction for robust nested object handling

- **Parameters:**
  - `data` (any): The input data to extract JSON from. Can be a dict, list, or str.
- **Returns:**
  - `dict` or `list`: A parsed JSON object (usually a dict or list).
- **Raises:**
  - `ValueError`: If no valid JSON can be extracted from the input.

## Text Service

The Text service provides functions to work with String data.

### Functions

#### `remove_tags_no_keep(text: str, start: str, end: str) -> str`

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

## Log Service

The Log service provides functionality for application logging with both file and console output.

### Functions

#### `setup_logging(app_name: str = "ACRA", log_level: int = logging.INFO) -> logging.Logger`

Configure logging for the application to write logs to a file with the current date in the name.

- **Parameters:**
  - `app_name` (str): Name of the application to include in log messages
  - `log_level` (int): Logging level (default: logging.INFO)
- **Returns:**
  - `logging.Logger`: The configured logger

#### `log_shutdown(app_name: str)`

Log a shutdown message to clearly mark the end of an execution.

- **Parameters:**
  - `app_name` (str): Name of the application to include in the shutdown message

#### `get_logger(name: str) -> logging.Logger`

Get a logger with the specified name, inheriting the root logger's configuration.

- **Parameters:**
  - `name` (str): Name for the logger, typically the module name
- **Returns:**
  - `logging.Logger`: A logger instance

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

## Ollama Export Utility

The Ollama Export Utility provides functionality to export Ollama models to zip files for easy transfer between different Ollama instances.

### Functions

#### `create_zip(ollamamodels, registry, repository, model_name, model_tag, output_zip)`

Creates a zip file containing all necessary files to transfer an Ollama model.

- **Parameters:**
  - `ollamamodels` (str): Path to the Ollama models directory
  - `registry` (str): The Ollama model registry (default: "registry.ollama.ai")
  - `repository` (str): Name of the repository (default: "library")
  - `model_name` (str): Name of the model (e.g., "gemma")
  - `model_tag` (str): Tag of the model (e.g., "2b")
  - `output_zip` (str): Output zip file name

### Usage

The utility can be used from the command line:

```sh
python export_ollama.py <model_name> <model_tag> [--ollamamodels PATH] [--registry REGISTRY] [--repository REPOSITORY] [--output OUTPUT_FILE]
```

Example:
```sh
python export_ollama.py gemma 2b --output gemma_2b_export.zip
```

The exported zip file can be imported to another Ollama instance using:
```sh
tar -xf <modelname>_<tag>_export.zip
```