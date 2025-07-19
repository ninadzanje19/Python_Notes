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

from constants import gemini_api_key
from langchain_google_genai import ChatGoogleGenerativeAI
llm_gemini = ChatGoogleGenerativeAI()
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

loader = TextLoader("data/knowledge_base.txt", encoding='utf-8')
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
