"""
Example of using the `utils` module for logging, command-line argument handling, and managing project constants.
The script also changes the CWD to the directory of the main script (the location from which the script is executed).

This script demonstrates how to:
1. Change the current working directory to the directory of the main script.
2. Set up logging using the `setup_logger` function from the `utils` module.
3. Log the application startup, the current working directory (CWD), and the parsed command-line arguments.
4. Use project constants defined in the `constants` module (e.g., paths and logging formats).
"""

from utils import setup_logger, args
from utils.constants import BASE_DIR

logger = setup_logger(__name__, 'app.log')

logger.info("Started")
logger.info("Current working directory: {}".format(BASE_DIR))
logger.info("Args: {}".format(str(args)))
