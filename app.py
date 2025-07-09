from pathlib import Path

from utils import setup_logger, args


logger = setup_logger(__name__, 'app.log')

logger.info("Started")
logger.info("Current working directory: {}".format(Path('.').resolve()))
logger.info("Args: {}".format(str(args)))
