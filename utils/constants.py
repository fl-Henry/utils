"""All the project constants"""

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
