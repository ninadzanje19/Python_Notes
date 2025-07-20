########################################################################################################################
#                           Splitters and Retrievers
########################################################################################################################
#Load tge Data
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
#Create the embeddings of the docs using InMemory Vector Store (For testing purposes vector db created in the RAM)
from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

#Checkout various embedding models at https://python.langchain.com/docs/integrations/text_embedding/
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Vectorize the docs
from langchain_community.vectorstores.inmemory import InMemoryVectorStore
vector_store = InMemoryVectorStore.from_documents(
    docs_split,
    embeddings,
)

retrieved_results = vector_store.as_retriever(search_type="mmr", k= 4)
response_retriever = retrieved_results.invoke("What is the flora of Savannah?")

#Checkout various vector stores at https://python.langchain.com/docs/integrations/vectorstores/
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Create the embeddings of the docs using ChromaDB
#Create the Chroma VectoreStore (Database)
from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
)

#To add items to the vector store we require each element from the doc split to have a unique ID
ids_of_docs = []
for ids in range(len(docs_split)):
    ids_of_docs.append(str(ids))

#Vectorize and add documents to the Chroma Vector Store
vector_store.add_documents(
    documents=docs_split,
    ids=ids_of_docs
)

#Get a document from the Vector Store
document_from_vector_store = vector_store.get(ids=str(1))

#Update the vector store by adding new a document
from langchain_core.documents import Document

updated_document = Document(
    page_content="Savannah is very important for the African enviornment",
    metadata={"source": "Geograpy Encyclopedia"},
)
"""When updating the vector store with a document, the id of the doc should be unique else it will replace the doc with same id"""
vector_store.update_document(document=updated_document,
                             document_id=str(67))

#Delete a document from the vector store
vector_store.delete(ids=[str(1)])

#Query the results (Get the similar results to the query)
results = vector_store.similarity_search(
    query="What animals live in the Savannah",
    k=2)

#Query by turning into retriever
retriever = vector_store.as_retriever(
    search_type="mmr", search_kwargs={"k": 1}                           #default value 4
)

retrieved_results = retriever.invoke("What animals live in the Savannah")
