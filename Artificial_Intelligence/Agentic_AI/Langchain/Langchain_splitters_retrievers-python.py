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
