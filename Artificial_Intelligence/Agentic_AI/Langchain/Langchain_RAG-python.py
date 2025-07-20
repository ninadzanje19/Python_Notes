########################################################################################################################
#                           RAG(Retrieval Argument Generation)
########################################################################################################################
"""
Process of RAG
    1. Load the data using langchain loaders
    2. Split the data into chunks using langchain splitters
    3. Create embeddings and Vectorize the chunks in the vector store
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                Do this once in the first time only
    4. Configure the langchain prompt runnable
    5. Configure the llm runnable
    6. Configure the output parser runnable
    7. Configure retriever and query as a runnable
    8. Create the chain
        prompt -> retriever -> llm -> output_parser
    9.Invoke the Chain
"""

#STEP 1 Load the data using langchain loaders
from langchain_community.document_loaders import TextLoader

loader = TextLoader("data/knowledge_base.txt", encoding='utf-8')
docs = loader.load()

#STEP 2 Split the data into chunks using langchain splitters
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=100,
                chunk_overlap=20,
                length_function=len,
                is_separator_regex=False
                )

docs_split = text_splitter.split_documents(docs)


#STEP 3 Create embeddings and Vectorize the chunks in the vector store
from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./rag_chroma_langchain_db"
)

ids_of_docs = []
for ids in range(len(docs_split)):
    ids_of_docs.append(str(ids))

#Vectorize and add documents to the Chroma Vector Store
vector_store.add_documents(
    documents=docs_split,
    ids=ids_of_docs
)

########################################################################################################################
#STEP 4 Configure the langchain prompt runnable
from langchain.prompts import PromptTemplate

#Create a prompt template
prompt_template = """Answer the question based only on the following context:
                     {context}
                     Question: {question}
                  """

prompt = PromptTemplate(
    input_variables=["question"],
    template=prompt_template
)

#STEP 5 Configure the llm runnable
from constants import gemini_api_key
from langchain_google_genai import ChatGoogleGenerativeAI
llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.0-flash",
                                    api_key=gemini_api_key)

#STEP 6 Configure the output parser runnable
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

#STEP 7 Configure retriever and query as a runnable
rag_retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 1})
query_and_results = {"context": (lambda x: x["question"]) | rag_retriever, "question": (lambda x: x["question"])}

#STEP 8 Create the chain (prompt -> retriever -> llm -> output_parser)
chain = query_and_results | prompt | llm_gemini | output_parser

#STEP 9 Invoke the Chain
result = chain.invoke({"question": "What animals are found in Savanna?"})
print(result)