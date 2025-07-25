# `utils` Module

The `utils` module provides utility functions for common tasks used across the project. It includes functions for setting up logging, handling command-line arguments, and managing directories. This module helps simplify and streamline operations in your Python application.

## Features
- **Current working directory**: Changes the current working directory (CWD) to `__main__` parent.
- **Directory Management**: Automatically manages and creates required directories (e.g., `data`, `temp`, and `logs`) if they don't exist, ensuring a smooth workflow for file handling.
- **Logging Setup**: Configures logging to both a file and stdout, allowing for easy debugging and monitoring of the application.
- **Command-line Argument Parsing**: Uses `argparse` to parse command-line arguments and make them accessible within the application.
- **Constant Definitions**: Includes predefined constants (e.g., directory paths, logging formats) used throughout the project for consistency.

## Installation

This module is part of the project and doesn't require installation via a package manager. To use it, simply import the relevant functions or constants.

## Usage

```python
from utils import setup_logger, args
from utils.constants import BASE_DIR

logger = setup_logger(__name__, 'app.log')

logger.info("Started")
logger.info("Current working directory: {}".format(BASE_DIR))
logger.info("Args: {}".format(str(args)))
```
