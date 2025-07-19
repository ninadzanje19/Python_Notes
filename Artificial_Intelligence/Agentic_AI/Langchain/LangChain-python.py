"""################LangChain theory################"""

"""
1. LangChain Overview
2. Chain, Prompts, Loaders
3. LCEL and Runnables
4. Splitters and Retrievers
5. RAG
6. Tools
7. Agents
"""

########################################################################################################################
#                                   Langchain Overview
########################################################################################################################
#pip install -U langchain-google-genai
#For Google Gemini only

from constants import  gemini_api_key

#LLM setup
from langchain_google_genai import ChatGoogleGenerativeAI
llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.0-flash",
                                    api_key=gemini_api_key)

# Simple text invocation
result = llm_gemini.invoke("What is Artificial Intelligence?")


system_prompt = "You will explain these topics to the user like he is a 5 year old child"
user_prompt = "What is Langchain?"

#Send a basic request using system and human/user messages
from langchain_core.messages import SystemMessage, HumanMessage
import textwrap

messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]

response = llm_gemini.invoke(messages)
answer = textwrap.fill(response.content, width=100)




