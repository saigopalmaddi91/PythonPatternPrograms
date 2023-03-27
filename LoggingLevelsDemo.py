import logging
logging.basicConfig(filename="loggingdemo.log", level=logging.DEBUG, filemode='w')

logging.critical("This is a CRITICAL Message")
logging.error("This is an ERROR message")
logging.warning("This is a WARNING message")
logging.info("This is an INFO message")
logging.debug("This is a DEBUG message")
