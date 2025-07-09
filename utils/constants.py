"""All the project constants

This module contains all the constants and directory paths used throughout the project.
It includes paths for base directories, data, temporary storage, and logs. The module
also includes format strings for logging and datetime formatting.

Constants are set up and directories are created if they do not already exist.

"""

from pathlib import Path

# [Dirs]
# Dir paths
BASE_DIR = Path('.').resolve()
DATA_DIR = BASE_DIR.joinpath('data').resolve()
TEMP_DIR = BASE_DIR.joinpath('temp').resolve()
LOG_DIR = TEMP_DIR.joinpath('logs').resolve()

# Create dirs
DATA_DIR.mkdir(exist_ok=True)
TEMP_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# [Logs]
LOG_FORMATTER = '%(asctime)s [%(levelname)s]: %(name)s: %(message)s'

# [Datetime]
DATETIME_FMT = '%Y-%m-%d-%H-%M-%S'
# TIME_FORMAT = 'ISO8601'

# [OTHER]
# Placeholder for additional constants or configurations
