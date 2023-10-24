import logging

logger = logging.getLogger("demologger")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s', datefmt='%d:%m:%Y %I:%M%S %p')
fileHandler = logging.FileHandler("filehands.txt", mode='w')
fileHandler.setLevel(40)

fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

logger.info("Information")
logger.debug("Debugging")
logger.warning("Warn")
logger.error("Errors")
logger.critical("Crucial")
