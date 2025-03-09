import os
from dotenv import load_dotenv
from src.data_ingestor.ingestor import load_data
from src.data_transformer.splitter import split_data_into_chunks
from src.data_transformer.embedder import convert_to_embedding_and_create_vs, get_retriever

from src.llm_core.model_functions import query_chatbot, generate_new_session_id


if __name__ == "__main__":
    load_dotenv()
    os.environ['HF_TOKEN'] = os.getenv('HF_TOKEN')
    #docs = load_data(os.getenv("input_data_dir"))
    #doc_split = split_data_into_chunks(docs)
    #retriever = convert_to_embedding_and_create_vs(doc_split, os.getenv("hf_embed_model"), os.getenv("vector_store_save_path"))

    session_id = generate_new_session_id()
    retriever = get_retriever(os.getenv("hf_embed_model"), os.getenv("vector_store_save_path"))

    print("Welcome to chatbot !!!")
    while True:
        user_input = input()
        if user_input == "bye":
            break
        else:
            response = query_chatbot(os.getenv("llm_model"), os.getenv("groq_api_key"), retriever, user_input, session_id)
            print(response)
