import os
import sys
from src.utils.logger import logging
from src.utils.exception import CustomException


def load_data(input_data_dir):

    try:
        data = []
        if not os.path.exists(input_data_dir):
            raise FileNotFoundError("Data Directory not found")
        else:
            logging.info("Input data extraction started")

    except FileNotFoundError as e:

        raise CustomException(e, sys)
