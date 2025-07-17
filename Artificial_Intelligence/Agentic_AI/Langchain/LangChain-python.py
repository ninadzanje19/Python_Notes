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
#Assemble the chain (prompt | llm)
#The function happening here is we are setting up a chain that gives our prompt to our llm
chain = prompt | llm_gemini

response = chain.invoke({"topic":"What is Langchain"}).content

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""Loaders"""
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
#                        Langchain Expression Language and Runnables
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

from langchain.prompts import PromptTemplate

#Standard process for creating a prompt
summarization_template = ("You are a helpful assistant that summarizes AI concepts."
                          "{context}"
                          "Summarize the context")

summarize_prompt = PromptTemplate.from_template(summarization_template)

"Runnable Sequence"
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()
chain = summarize_prompt | llm_gemini | output_parser           #Basic Runnable sequence

response_of_runnable_sequence = chain.invoke({"context": "What is Langchain?"})

"""
Here the prompt is passed to the llm_gemini and the output is further passed to output_parser
Which properly parses the output.

Prompt -> Gemini processes the prompt -> Parses the prompt properly
"""
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"Runnable Lambda"
from langchain_core.runnables import RunnableLambda

#Create a lambda function and create a RunnableLambda object
length_lambda = RunnableLambda(lambda summary_length: f"Summary length: {len(summary_length)} characters")

#Chain the lambda function to the existing chain
lambda_chain = summarize_prompt | llm_gemini | output_parser | length_lambda

response_lambda = lambda_chain.invoke({"context": "What is Langchain?"})

"""
Here the existing chain's output's length is taken.
Prompt -> Gemini processes the prompt -> Parses the prompt properly -> length is calculated
"""
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"Runnable Passthrough"
from langchain_core.runnables import RunnablePassthrough

#Create a RunnablePassthrough object
passthrough = RunnablePassthrough()

#Chain the passthrough object to the existing chain
passthrough_chain_unchanged = summarize_prompt | llm_gemini | output_parser | passthrough

response_passthrough_unchanged = passthrough_chain_unchanged.invoke({"context": "What is Langchain?"})

"""
Here the passthrough object is chained to the existing chain as a placeholder
Prompt -> Gemini processes the prompt -> Parses the prompt properly -> placeholder(does nothing)
"""

#Define  lambda function that maps {"key" to value}
passthrough_lambda_function = RunnableLambda(lambda summary: {"summary": summary})

assign_passthruugh = RunnablePassthrough.assign(length = lambda x: len(x["summary"]))

passthrough_chain_changed = summarize_prompt | llm_gemini | output_parser | passthrough_lambda_function | assign_passthruugh

response_passthrough_changed = passthrough_chain_changed.invoke({"context": "What is Langchain?"})

"""
Here the passthrough objet is chained to the existing chain as a function that maps the summary and its length as {summary: , length: }
We are modifying the output.
Instead of the default return from output parser we change the output to a custom dictionary.
Prompt -> Gemini processes the prompt -> Parses the prompt properly -> placeholder(maps the summary and its length as {summary: , length: })
"""

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"Runnable Parallel"
from langchain_core.runnables import RunnableParallel

parallel_runnable = RunnableParallel(
                    summary=lambda x: x,
                    length=lambda x: len(x)
                    )

parallel_chain = summarize_prompt | llm_gemini | output_parser | parallel_runnable

response_parallel = parallel_chain.invoke({"context": "What is Langchain?"})

########################################################################################################################
#                           Splitters and Retrievers
########################################################################################################################
from langchain_community.document_loaders import TextLoader

loader = TextLoader("knowledge_base.txt", encoding='utf-8')
docs = loader.load()

from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=100,                                 #Each chunk is of max this much chars
                chunk_overlap=20,                               #Consecutive chunks will share this much chars to maintain context
                length_function=len,
                is_separator_regex=False                        #separators used for splitting are treated as plain strs (\n)
                )

docs_split = text_splitter.split_documents(docs)

#Checkout various loaders at https://python.langchain.com/docs/integrations/document_loaders/
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

#Checkout various embedding models at https://python.langchain.com/docs/integrations/text_embedding/
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from langchain_community.vectorstores.inmemory import InMemoryVectorStore
vector_store = InMemoryVectorStore.from_documents(
    docs_split,
    embeddings,
)

retrieved_results = vector_store.as_retriever(search_type="mmr", k= 4)
response_retriever = retrieved_results.invoke("What is the flora of Savannah?")

#Checkout various vector stores at https://python.langchain.com/docs/integrations/vectorstores/
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

########################################################################################################################
#                           RAG(Retrieval Argument Generation)
########################################################################################################################
"""
Process of RAG
    1. Load the data using langchain loaders
    2. Split the data into chunks using langchain splitters
    3. Vectorize the chunks in the vector store
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                Do this once in the first time only
    4. Configure the langchain prompt runnable
    5. Configure the llm runnable
    6. Configure the output parser runnable
    7. Configure the runnable lambda function if required for any additional functionality
    8. Configure any passthroughs or parallels if required
    9. Create the chain 
        prompt -> retriever -> llm -> output_parser 
"""

#create a prompt runnable (component)
from langchain.prompts import  ChatPromptTemplate
rag_template = """
                Answer the following question based upon the given context: {context}
                Question: {question}
               """

rag_prompt = ChatPromptTemplate.from_template(rag_template)

#Configure the llm runnable (component)
rag_llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


#create a output parser runnable (component)
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

rag_query = "What is the flora of Savannah"

#Create the retriever runnable lambda (component)
rag_retrieved_results = vector_store.as_retriever(search_type="mmr", k= 4)

#Create the RAG chain
rag_chain = ({"context": (lambda x: x["question"]) | rag_retrieved_results,
              "question": (lambda x: x["context"])} | rag_prompt | rag_llm | output_parser

)
print(rag_chain.invoke(rag_query))
########################################################################################################################
#                                               Tools
########################################################################################################################

"""Duck Duck Go search"""
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

response_tools = search.invoke("Tell me about Langchain")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""Serp Search"""
from langchain_community.utilities import SerpAPIWrapper
from constants import serp_api_key


params = {
    "engine": "google",
    "gl": "in",
    "hl": "en",
}
serp_search = SerpAPIWrapper(serpapi_api_key=serp_api_key,params=params)
#response_tools = serp_search.run("Tell me about Langchain")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""Serper Search (Paid)"""
from constants import serper_api_key
import os
os.environ["SERPER_API_KEY"] = serper_api_key
from langchain_community.utilities import GoogleSerperAPIWrapper

serper_search = GoogleSerperAPIWrapper()
#response_tools = serper_search.run("Tell me about Langchain")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""Brave Search"""
from langchain_community.tools import BraveSearch
from constants import brave_api_key

tool = BraveSearch.from_api_key(api_key=brave_api_key, search_kwargs={"count": 3})
#response_tools = tool.run("Tell me about Langchain")

#Checkout various tools at https://python.langchain.com/docs/integrations/tools/
########################################################################################################################
#                                               Agents
########################################################################################################################
