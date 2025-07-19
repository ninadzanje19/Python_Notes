########################################################################################################################
#                               Chains, Prompts and Loaders
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

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""Prompts"""
#Langchain provides a powerful class PromptTemplate which basically modifies our simple given prompt
from langchain.prompts import PromptTemplate

#Create a prompt template
prompt_template = ("You are a helpful assistant that explains AI topics."
                   "Given the following input {topic}."
                   "Provide the explanation of the given topic")

#Create prompt from prompt templates (This converts your simple text prompt to the format suitable for Langchain to process)
prompt = PromptTemplate(
    input_variables=["topic"],                  #What is going to be your input
    template=prompt_template
)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""Chains"""
from constants import gemini_api_key
from langchain_google_genai import ChatGoogleGenerativeAI
llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.0-flash",
                                    api_key=gemini_api_key)

#Assemble the chain (prompt | llm)
#The function happening here is we are setting up a chain that gives our prompt to our llm
chain = prompt | llm_gemini

response = chain.invoke({"topic":"What is Langchain"}).content

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""Loaders"""
#In LangChain we are given inbuilt loaders class that helps us to load data for our application
from langchain_community.document_loaders import csv_loader

loader = csv_loader.CSVLoader("data/random_data.csv")
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
