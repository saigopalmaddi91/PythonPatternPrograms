import logging

# Creating custom logger other than root logger involves 5 steps
# 1. create logger object and set level
logger = logging.getLogger("demologger")
logger.setLevel(logging.DEBUG)  # default NOTSET(0), all messages will be considered

# 2. create handler object and set level

consoleHandler = logging.StreamHandler()  # log message displayed in console
# consoleHandler.setLevel(logging.ERROR)

fileHandler = logging.FileHandler('customlogger.log', mode='w')  # log messages written to file
# fileHandler.setLevel(logging.ERROR)

# 3. create formatter object and set level

formatHandler = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S %p')
formatter = logging.Formatter('%(levelname)s : %(message)s')
# 4. set Formatter to Handler

consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatHandler)

# 5. Add Handler to Logger

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

# 6. Write log messages by logger object

logger.critical("This is CRITICAL log")
logger.error("This is ERROR log")
logger.warning("This is WARNING log")
logger.info("This is INFO log")
logger.debug("This is DEBUG log")
