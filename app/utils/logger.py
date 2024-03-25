"""custom logging for the whole fastapi app"""

import logging
import sys

# get the logging instance
logger = logging.getLogger()

# create format
format = logging.Formatter(fmt="%(levelname)s: %(asctime)s - %(message)s")

# create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("app.log")

# set formatter
stream_handler.setFormatter(format)
file_handler.setFormatter(format)

# add the handlers to the logger
logger.handlers = [stream_handler, file_handler]

# set level
logger.setLevel(logging.INFO)
