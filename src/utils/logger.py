import inspect
import logging
import os
import atexit

LOG_FILE_NAME = "automation.log"
_logs_cleared = False  # Track if logs have been cleared in this session


def create_formatter():
    """Create and return a logging formatter"""
    return logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s: %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p'
    )


def clear_logs(log_file=LOG_FILE_NAME):
    """Clear the contents of the log file"""
    try:
        open(log_file, 'w').close()
    except Exception as e:
        print(f"Error clearing log file: {e}")


def custom_logger(log_level=logging.DEBUG, log_file=LOG_FILE_NAME, clear_existing=False):
    """
    Create and return a custom logger
    
    Args:
        log_level: Logging level for the file handler
        log_file: Path to the log file
        clear_existing: If True, clear existing logs before creating logger
    """
    global _logs_cleared
    
    # Clear logs only once at the start of the session
    if not _logs_cleared:
        clear_logs(log_file)
        _logs_cleared = True

    # Still honor explicit clear request
    if clear_existing:
        clear_logs(log_file)

    caller_name = inspect.stack()[1][3]
    logger = logging.getLogger(caller_name)
    logger.setLevel(logging.DEBUG)

    # Remove existing handlers to avoid duplicate logging
    logger.handlers = []

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)

    formatter = create_formatter()
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger


# Reset the cleared flag when the Python interpreter exits
def _reset_logs_cleared():
    global _logs_cleared
    _logs_cleared = False

atexit.register(_reset_logs_cleared)
