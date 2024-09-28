import logging 
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # log file ka nam month day hour minutes second ke form me hoga.
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)# jaise code run hoga ek logs folder bnega aur log file usme store hogi automatic.
os.makedirs(logs_path,exist_ok=True)# ye use horha taki ye folder file ban skey apne environment me.

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)