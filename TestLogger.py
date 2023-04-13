from customlogger import get_custom_logger

import logging


def logtest():
    logger = get_custom_logger(logging.DEBUG)
    logger.critical("CRITICAL message from TestLogger module")
    logger.error("ERROR message from TestLogger module")
    logger.warning("WARNING message from TestLogger module")
    logger.info("INFO message from TestLogger module")
    logger.debug("DEBUG message from TestLogger module")

logtest()