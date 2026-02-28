import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return None

    os.environ["GROQ_API_KEY"] = api_key

    return ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.3,
        max_tokens=1024
    )