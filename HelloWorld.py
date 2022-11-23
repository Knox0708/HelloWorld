import logging
import os
HW = os.environ['HW']
logging.basicConfig(level=logging.DEBUG, filemode='w', encoding='utf-8', filename='HW.log')

logging.info(HW)

