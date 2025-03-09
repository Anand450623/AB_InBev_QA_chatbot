# AB_InBev_QA_chatbot
This is solution submission for AB_InBev_QA_chatbot assignment

# Task Detail:
1. Logging and Custom Exception Handling -> done
2. Code Modularisation -> done
3. Stateful ChatBot Implementation -> done
4. FastApi Integration -> done (Bonus)
5. Docker Integration & deployment -> done (Bonus)

# Code Setup:

1. Clone the repository with git clone command. (git clone https://github.com/Anand450623/AB_InBev_QA_chatbot.git)
2. cd AB_InBev_QA_chatbot
3. python -m venv venv
4. Activate virtual env (Commands for this slightly differ from OS to OS, please check as per yours).
5. python install -r requirements.txt
6. python app:app --reload

# NOTE:
All the keys and model names are to be taken from .env file which can't be pushed, so below is the list of env variables that the code expects and also I'm giving a sample of how to execute. For Actual execution of code, values has to be passed.

docker build -t {your_image_name} .

docker run --rm \
-e HF_TOKEN={value} \
-e input_data_dir=demo_bot_data \
-e hf_embed_model={value} \
-e vector_store_save_path=resources/vector_store \
-e llm_model={value} \
-e groq_api_key={value} \
-p 8000:8000 \
{your_image_name}

# screenshots

1. Swagger UI on Docker:

![image](https://github.com/user-attachments/assets/dd75ff9d-2cb0-4002-99ca-985b37b570eb)

2. ChatBot Option:
  2.1 user_query (str): The question user wants to ask.
  2.2 new_conversation (bool): If the user wants to start a new chat(true) or continue with existing (false)
  2.3 prev_session_id (str) -> Optional: This is optional when you're starting a new chat, otherwise user has to pass, with each answer the model also responds back the session_id. User can copy paste the same id to continue in the same communication.

First Interaction with Chatbot:

![image](https://github.com/user-attachments/assets/b0c97805-6c47-41a3-b18d-3960781b4a1e)

3. Follow up conversation using same session-id:

![image](https://github.com/user-attachments/assets/681ed179-0d8f-4573-ac14-fdc7ec684a18)

4. Summarisation of conversation:

![image](https://github.com/user-attachments/assets/c0593925-09eb-4726-ac61-00f176d52363)

5. Starting a new conversation, please note that since this is a new conversation, the model doesn't have any prior infomation to this and therefore provides a generic answer instead like the last time. And also, a new session id is generated and is provided back to user as response.

![image](https://github.com/user-attachments/assets/2134996d-bf47-4c18-86cb-f5c9857cedef)







