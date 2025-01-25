"""
logging: A Python module to log messages, which is useful for tracking events in an application. Logs can store information about errors, warnings, or other events for debugging or monitoring purposes.

"""


import logging # It is used for tracking purpose. even the custome exceptions are tracked.
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok = True)

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s %(levelname)s %(message)s',  # Standard fields
    level=logging.INFO,
)


if __name__ == "__main__":
    logging.info("Logging")