import os
from dotenv import load_dotenv
from src.data_ingestor.ingestor import load_data
from src.data_transformer.splitter import split_data_into_chunks
from src.data_transformer.embedder import convert_to_embedding_and_create_vs, test_vs_store


if __name__ == "__main__":
    load_dotenv()
    os.environ['HF_TOKEN'] = os.getenv('HF_TOKEN')
    #docs = load_data(os.getenv("input_data_dir"))
    #doc_split = split_data_into_chunks(docs)
    #retriever = convert_to_embedding_and_create_vs(doc_split, os.getenv("hf_embed_model"), os.getenv("vector_store_save_path"))
    #print(retriever)

    test_vs_store(os.getenv("hf_embed_model"), os.getenv("vector_store_save_path"),"how to install ubuntu")
