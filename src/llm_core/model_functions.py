import random
import string
from langchain_groq import ChatGroq
from langchain_core.messages import trim_messages
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain, create_history_aware_retriever


store = {}


def generate_new_session_id():
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(10))
    return random_string


def get_session_history(session_id: str) -> BaseChatMessageHistory:

    if session_id not in store:
        store[session_id] = ChatMessageHistory()

    return store[session_id]


def query_chatbot(llm_model, groq_api_key, retriever, user_query, session_id):

    llm = ChatGroq(groq_api_key=groq_api_key, model_name=llm_model)

    contextualize_q_system_prompt = (
        "Given a chat history and the latest user question"
        "which might reference context in the chat history, "
        "formulate a standalone question which can be understood "
        "without the chat history, Do NOT answer the question, "
        "just reformulate it if needed and otherwise return it as is."
    )

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)

    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer the question in the best possible manner."
        "If you don't know the answer, say that you don't know."
        "\n\n"
        "{context}"
    )

    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}")
        ]
    )

    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

    def trim_history(history):
        trimmer = trim_messages(
            max_tokens=2,
            strategy="last",
            token_counter=llm,
            include_system=True,
            start_on="human",
        )
        return trimmer.invoke(history)

    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
        history_transform=trim_history
    )

    response = conversational_rag_chain.invoke(
        {"input": user_query},
        config={
            "configurable": {"session_id": session_id}
        },
    )

    print(response.keys())
    print(len(response['chat_history']))
    print(response['chat_history'])

    return response["answer"]
