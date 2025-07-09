import logging
from . import const


def setup_logger(name, log_file=None, log_level=logging.INFO):
    """
    Configures logging to log messages to both a file and stdout.

    This function sets up a logger that can log messages to both the standard
    output (stdout) and a log file, with customizable logging levels. The
    logger will use the format defined in `const.LOG_FORMATTER` for both
    output channels.

    :param name: str
        Name of the logger, which is used to identify the logger in log messages.

    :param log_file: str, optional
        The name of the log file where log messages will be written. If not
        provided, no file logging will be set up. The file will be saved in
        the directory specified by `const.LOG_DIR`.

    :param log_level: int, optional
        The logging level to use for both the file and stream handlers. This
        controls the severity of messages that will be logged. Default is
        `logging.INFO`. Other options include `logging.DEBUG`, `logging.WARNING`,
        `logging.ERROR`, and `logging.CRITICAL`.

    :return: logging.Logger
        The configured logger that can be used to log messages.
    """
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Formatter using the format defined in const.LOG_FORMATTER
    formatter = logging.Formatter(const.LOG_FORMATTER)

    # File handler setup (if log_file is provided)
    if log_file is not None:
        log_file = const.LOG_DIR.joinpath(log_file)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Stream (stdout) handler setup
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
