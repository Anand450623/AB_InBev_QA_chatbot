import os
from fastapi import FastAPI
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from src.data_ingestor.ingestor import load_data
from src.model.Response import Response
from src.data_transformer.splitter import split_data_into_chunks
from src.data_transformer.embedder import convert_to_embedding_and_create_vs, get_retriever
from src.llm_core.model_functions import query_chatbot, generate_new_session_id


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    os.environ['HF_TOKEN'] = os.getenv('HF_TOKEN')
    docs = load_data(os.getenv("input_data_dir"))
    doc_split = split_data_into_chunks(docs)
    convert_to_embedding_and_create_vs(doc_split, os.getenv("hf_embed_model"), os.getenv("vector_store_save_path"))

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/chatbot", response_model=Response)
async def chatbot(user_query : str, new_conversation : bool, prev_session_id=None):
    load_dotenv()
    retriever = get_retriever(os.getenv("hf_embed_model"), os.getenv("vector_store_save_path"))
    if new_conversation:
        session_id = generate_new_session_id()
        response = query_chatbot(os.getenv("llm_model"), os.getenv("groq_api_key"), retriever, user_query, session_id)

        return Response(
            status="Success",
            message="query executed successfully",
            data={
                "query_response": response,
                "session_id": session_id
            },
            errors=None
        )
    else:
        response = query_chatbot(os.getenv("llm_model"), os.getenv("groq_api_key"), retriever, user_query, prev_session_id)

        return Response(
            status="Success",
            message="query executed successfully",
            data={
                "query_response": response,
                "session_id": prev_session_id
            },
            errors=None
        )

