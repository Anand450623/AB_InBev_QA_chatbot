import sys
from src.utils.logger import logging
from src.utils.exception import CustomException
from langchain_text_splitters import MarkdownTextSplitter


def split_data_into_chunks(docs):

    try:
        logging.info("Splitting/Chunking process Initiated")
        doc_splitter = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=100)
        split_doc = doc_splitter.split_documents(docs)
        logging.info(f"Splitting/Chunking process Completed, final split doc size = {len(split_doc)}")
        return split_doc
    except Exception as e:
        raise CustomException(e, sys)
