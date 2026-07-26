import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CHROMA_DB = os.getenv("CHROMA_DB", "vector_db")

PDF_FOLDER = os.getenv("PDF_FOLDER", "data")

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1")