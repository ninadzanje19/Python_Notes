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
#For Google Gemini only

from dotenv import load_dotenv

load_dotenv()

#LLM setup
from langchain_google_genai import ChatGoogleGenerativeAI

llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

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

########################################################################################################################
########################################################################################################################
########################################################################################################################

"""
In LangChain the components are often referred to as Runnables.
These Runnables can be chained together.
These are:
1. Prompts              (Which the user gives)
2. LLMs                 (Gemini, Llama, OpenAI, etc) 
3. Output Parsers       (structure the output)
4. External Tools       (Additional tools)
5. General Function     (Additional Functions used)
"""

#Langchain provides a powerful class PromptTemplate which basically modifies our simple given prompt
from langchain.prompts import PromptTemplate

#Create a prompt template
prompt_template = ("You are a helpful assistant that explains AI topics."
                   "Given the following input {topic}."
                   "Provide the explanation of the given topic")

#Create prompt from prompt templates
prompt = PromptTemplate(
    input_variables=["topic"],                  #What is going to be your input
    template=prompt_template
)

#Assemble the chain (prompt | llm)
#The function happening here is we are setting up a chain that gives our prompt to our llm
chain = prompt | llm_gemini

response = chain.invoke({"topic":"What is Langchain"}).content


#In LangChain we are given inbuilt loaders class that helps us to load data for our application
from langchain_community.document_loaders import csv_loader

loader = csv_loader.CSVLoader("random_data.csv")
docs = loader.load()

#Setup a chain using document loaders and llm
prompt_template = """You are a helpful assistant that explains CSV files. Given the following csv transcript:
                     {csv_transcript}
                     Give a summary."""
prompt = PromptTemplate(
            input_variables=["csv_transcript"],
            template=prompt_template
        )

chain = prompt | llm_gemini
response_of_loaders = chain.invoke({"csv_transcript": docs}).content

########################################################################################################################
########################################################################################################################
########################################################################################################################

"""
The LCEL (LangChain Expression Language) is a declarative way to compose Runnables into chains.
The Runnables are joined together using the | operator

A Runnable is a unit of work that can be invoked, batched, streamed, transformed and composed.
Instead of a Runnable we can feed a custom function on it.

The following are teh main classes in Lanchain:
RunnableSequence: Basic Runnable class. Chains together the Runnable component and makes sure the output of the 
                  Runnable component is passed to the next Runnable component.

RunnableLambda: Turns a Python function into Runnable component.

RunnablePassthrough: Keeps the input unchanged or modifies the input that goes into the Runnable component

RunnableParallel: Executes the multiple Runnable components concurrently. Allows us to branch the flow allowing us to 
                  get multiple outputs using single input.
"""