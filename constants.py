from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GOOGLE_API_KEY")
open_ai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")