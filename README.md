# AB_InBev_QA_chatbot
This is solution submission for AB_InBev_QA_chatbot assignment

# Task Detail:
1. Logging and Custom Exception Handling -> done
2. Code Modularisation -> done
3. Stateful ChatBot Implementation -> done
4. FastApi Integration -> done (Bonus)
5. Docker Integration & deployment -> done (Bonus)

# NOTE:
All the keys and model names are to be taken from .env file which can't be pushed, so below is the list of env variables that the code expects and also I'm giving a sample of how to execute. For Actual execution of code, values has to be passed.

docker build -t {your_image_name} .

docker run --rm /\
-e HF_TOKEN={value} \
-e input_data_dir=demo_bot_data \
-e hf_embed_model={value} \
-e vector_store_save_path=resources/vector_store \
-e llm_model={value} \
-e groq_api_key={value} \
-p 8000:8000 \
{your_image_name}

# screenshots

1. Swagger UI:

![image](https://github.com/user-attachments/assets/dd75ff9d-2cb0-4002-99ca-985b37b570eb)


