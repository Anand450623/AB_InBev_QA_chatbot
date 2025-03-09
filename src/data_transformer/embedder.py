import sys
from src.utils.logger import logging
from src.utils.exception import CustomException
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def convert_to_embedding_and_create_vs(doc_splits, hf_embed_model, vector_store_save_path):

    try:
        logging.info(f"Using Hugging Face {hf_embed_model} model for embedding")
        embeddings = HuggingFaceEmbeddings(model_name=hf_embed_model)
        logging.info(f"creating FAISS vector store using OS hugging Face embedding model")
        vector_store = FAISS.from_documents(doc_splits, embeddings)
        vector_store.save_local(vector_store_save_path)
        logging.info(f"vector store created and stored at {vector_store_save_path}")
        return vector_store.as_retriever()
    except Exception as e:
        raise CustomException(e, sys)


def get_retriever(hf_embed_model, vector_store_save_path):
    logging.info(f"fetching vector store from {vector_store_save_path}")
    embeddings = HuggingFaceEmbeddings(model_name=hf_embed_model)
    db = FAISS.load_local(vector_store_save_path, embeddings, allow_dangerous_deserialization=True)
    db_retriever = db.as_retriever()
    logging.info(f"vector store fetched from {vector_store_save_path}")
    return db_retriever
