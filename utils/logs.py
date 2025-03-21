import logging

from . import const


def setup_logger(name, log_file=None, log_level=logging.INFO):
    """Configures logging to log messages to both a file and stdout.

    :param name: str  Name of the logger.
    :param log_file: str  The name of the log file.
    :param log_level: int  The logging level, e.g., logging.DEBUG or logging.INFO.
    """
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    formatter = logging.Formatter(const.LOG_FORMATTER)

    # File handler
    if log_file is not None:
        log_file = const.LOG_DIR.joinpath(log_file)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Stream (stdout) handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
