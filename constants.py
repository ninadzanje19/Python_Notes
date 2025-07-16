from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GOOGLE_API_KEY")
open_ai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

hugging_face_token = os.getenv("HUGGING_FACE_TOKEN")

weviate_api_key = os.getenv("WEVIATE_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
redis_api_key = os.getenv("REDIS_API_KEY")

brave_api_key = os.getenv("BRAVE_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")
serp_api_key = os.getenv("SERP_API_KEY")