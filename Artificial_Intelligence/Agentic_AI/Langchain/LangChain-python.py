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

#pip install -U langchain-google-genai

from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Simple text invocation
result = llm_gemini.invoke("What is Artificial Intelligence?")


system_prompt = "You will explain these topics to the user like he is a 5 year old child"
user_prompt = "What is Langchain?"

from langchain_core.messages import SystemMessage, HumanMessage
import textwrap

messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]

response = llm_gemini.invoke(messages)
answer = textwrap.fill(response.content, width=100)



from langchain.prompts import PromptTemplate

#Create a prompt template
prompt_template = ("You are a helpful assistant that explains AI topics."
                   "Given the following input {topic}."
                   "Provide the explanation of the given topic")

#Create prompt from prompt templates
prompt = PromptTemplate(
    input_variables=["topic"],
    template=prompt_template
)

#Assemble the chain (prompt | llm)
chain = prompt | llm_gemini

response = chain.invoke({"topic":"What is Langchain"}).content

print(response)