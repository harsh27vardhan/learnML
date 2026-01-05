import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_PATH = os.path.join(os.getcwd(),"logs",LOG_FILE)
#os.getcwd() returns the current working directory
os.makedirs(LOG_PATH,exist_ok=True)  #this says that even though there is a file exists, keeps the files appeding inside that wherrever we want to create the file.

LOG_FILE_PATH = os.path.join(LOG_PATH,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,  # wherever we use logging or logging.info, it will log the info in the file
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

if __name__=="__main__":
    logging.info("Logging has started")