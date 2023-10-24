import logging

logger = logging.getLogger("demologger")
logger.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s', datefmt='%d:%m:%Y %I:%M%S %p')
consoleHandler = logging.StreamHandler()

consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

logger.info("Information")
logger.debug("Debugging")
logger.warning("Warn")
logger.error("Errors")
logger.critical("Crucial")
