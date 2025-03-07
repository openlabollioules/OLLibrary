"""
Configuration Manager Module
"""
import os
import json

class Config:
    """
    Configuration Manager Class

    Manages application configuration through a JSON file system. Provides
    functionality to load, save, and manipulate configuration settings persistently.

    Attributes
    ----------
    config_file : str
        Full path to the JSON configuration file.
    config : dict
        Dictionary containing the current configuration settings.
    """

    def __init__(self, config_dir: str = None):
        """
        Initialize a Config instance.

        Creates the data directory if it doesn't exist and loads the configuration
        from a JSON file.

        Parameters
        ----------
        config_dir : str
            Directory path where the configuration file will be stored.

        Notes
        -----
        If `config_dir` does not exist, it will be created.
        """
        if config_dir is None:
            config_dir = ".config"
        os.makedirs(config_dir, exist_ok=True)
        self.config_file = os.path.join(config_dir, "config.json")
        self.config = {}
        self.load_config()

    def load_config(self):
        """
        Load configuration from a JSON file.

        Reads the JSON configuration file and loads its content into the `config`
        attribute. If the file does not exist, initializes an empty configuration.

        Notes
        -----
        The configuration file must be in valid JSON format.
        """
        if os.path.exists(self.config_file):
            with open(self.config_file, "r", encoding="utf-8") as f:
                self.config = json.load(f)
        else:
            self.config = {}

    def save_config(self):
        """
        Save the current configuration to a JSON file.

        Writes the content of the `config` attribute to the JSON configuration file
        in a human-readable format.
        """
        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=4)

    def get(self, key, default=None):
        """
        Retrieve a configuration value by key.

        Parameters
        ----------
        key : str
            The key for the configuration parameter.
        default : Any, optional
            Default value to return if the key is not found.

        Returns
        -------
        Any
            The value associated with the key if it exists, otherwise `default`.
        """
        return self.config.get(key, default)

    def set(self, key, value):
        """
        Set a configuration value and save the configuration.

        Sets or updates a configuration parameter and immediately saves the
        updated configuration to the JSON file.

        Parameters
        ----------
        key : str
            The key for the configuration parameter.
        value : Any
            The value to set for the configuration parameter.
        """
        self.config[key] = value
        self.save_config()

    def show_config(self):
        """
        Return a formatted JSON string of the current configuration.

        Returns
        -------
        str
            A JSON formatted string representing the current configuration.
        """
        return json.dumps(self.config, indent=4)