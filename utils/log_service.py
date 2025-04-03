import os
import logging
import logging.handlers
import atexit
from datetime import datetime
import sys

# Global logger
logger = logging.getLogger()

def setup_logging(app_name="ACRA", log_level=logging.INFO):
    """
    Configure logging for the application to write logs to a file with the current date in the name.
    
    Args:
        app_name (str): Name of the application to include in log messages
        log_level (int): Logging level (default: logging.INFO)
        
    Returns:
        logging.Logger: The configured logger
    """
    # Create logs directory if it doesn't exist
    logs_dir = os.path.abspath(os.path.join(os.getcwd(), "logs"))
    os.makedirs(logs_dir, exist_ok=True)
    
    # Configure the current date for the log filename
    current_date = datetime.now().strftime("%d_%m_%Y")
    log_filename = os.path.join(logs_dir, f"log_{current_date}.log")
    
    # Configure the root logger
    global logger
    logger.setLevel(log_level)
    
    # Clear any existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    # Create a file handler that logs to the dated log file
    file_handler = logging.FileHandler(log_filename, encoding='utf-8')
    file_handler.setLevel(log_level)
    
    # Create a console handler
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setLevel(log_level)
    
    # Create a formatter and set it for both handlers
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    # Log startup message
    separator = "-" * 80
    logger.info(separator)
    logger.info(f"{app_name} STARTUP - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(separator)
    
    # Register the shutdown function
    atexit.register(log_shutdown, app_name)
    
    return logger

def log_shutdown(app_name):
    """
    Log a shutdown message to clearly mark the end of an execution.
    
    Args:
        app_name (str): Name of the application to include in the shutdown message
    """
    separator = "-" * 80
    logger.info(separator)
    logger.info(f"{app_name} SHUTDOWN - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(separator)

def get_logger(name):
    """
    Get a logger with the specified name, inheriting the root logger's configuration.
    
    Args:
        name (str): Name for the logger, typically the module name
        
    Returns:
        logging.Logger: A logger instance
    """
    return logging.getLogger(name) 