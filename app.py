import os
from dotenv import load_dotenv
from src.data_ingestor.ingestor import load_data


if __name__ == "__main__":
    load_dotenv()
    load_data(os.getenv("input_data_dir"))
