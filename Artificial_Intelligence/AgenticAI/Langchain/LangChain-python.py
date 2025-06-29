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

from dotenv import load_dotenv
load_dotenv()

from
llm_gpt4 = ChatOpenAI(model_name="gpt-4o")

response = llm_gpt4.invoke("What is LangChain?").content
print(response)