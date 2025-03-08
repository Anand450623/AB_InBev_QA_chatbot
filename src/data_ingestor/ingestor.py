import os
import sys
from pathlib import Path
from collections import deque
from src.utils.logger import logging
from src.utils.exception import CustomException
from langchain_community.document_loaders import UnstructuredMarkdownLoader


def load_data(input_data_dir):

    try:
        docs = []
        if not os.path.exists(input_data_dir):
            raise FileNotFoundError("Data Directory not found")
        else:

            logging.info("input data extraction initiated...")
            dir_queue = deque()
            dir_queue.append(input_data_dir)
            while dir_queue:
                curr_dir = dir_queue.popleft()
                files = os.listdir(curr_dir)
                for file in files:
                    file_path = curr_dir+"/"+file
                    path = Path(file_path)
                    if path.is_dir():
                        logging.info(f"Directory found at = {file_path}")
                        dir_queue.append(file_path)
                    else:
                        if file_path.endswith(".md"):
                            logging.info(f"Extracting markdown data from = {file_path}")
                            docs.extend(UnstructuredMarkdownLoader(file_path).load())

        logging.info(f"input data extraction completed successfully, {len(docs)} documents extracted")
        return docs

    except FileNotFoundError as e:

        raise CustomException(e, sys)
