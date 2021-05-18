import logging
import os

from datetime import datetime

# parent_dir = os.path.dirname(os.path.abspath(__file__))

# start_time = datetime.now()
# timestamp = start_time.strftime("%y-%m-%d_%H_%M_%S")

# log_dir = os.path.join(parent_dir, "logs")
# if not os.path.isdir(log_dir):
#     os.mkdir(log_dir)

# # log configuration
# file_handler = logging.FileHandler(os.path.join(log_dir,__name__ + timestamp))
# console_handler = logging.StreamHandler()
# formatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
# file_handler.setFormatter(formatter)
# console_handler.setFormatter(formatter)
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)
# log configuration

DIR = os.path.dirname(os.path.abspath(__file__))

start_time = datetime.now()
timestamp = start_time.strftime("%y-%m-%d_%H_%M_%S")

log_dir = os.path.join(DIR, "logs")
if not os.path.isdir(log_dir):
    os.mkdir(log_dir)

file_handler = logging.FileHandler(os.path.join(log_dir, "dominizer_" + timestamp))
console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
#logger.addHandler(console_handler)