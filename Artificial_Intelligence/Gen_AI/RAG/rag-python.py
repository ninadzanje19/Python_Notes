##################################STEP 1##################################
"""********************Break your data into chunks*********************"""
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Your large text string
with open("document.txt", "r", encoding="utf-8") as doc_text:
    doc_text = doc_text.read()

# Create the splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,       # Customize depending on your model
    chunk_overlap=50      # Helps maintain context between chunks
)

# Create the chunks
chunks = text_splitter.create_documents([doc_text])

##################################STEP 2##################################
"""********************Convert the data chunks to vector embeddings*********************"""
from chromadb.utils import embedding_functions

#Configure the embedding function
embedding_fn = embedding_functions.DefaultEmbeddingFunction()

#Create the documents i.e. Divide your main document into smaller chunks
documents = []
for chunk in chunks:
    documents.append(chunk.page_content)

#Pass the documents to the embedding function to create embeddings
embeddings = embedding_fn(documents)


#Generate unique ids for each embedding. {len(ids) == len(embeddings)}

ids = []
for number in range(len(embeddings)):
    ids.append(str(number))

##################################STEP 3##################################
"""********************Store and query the vector embeddings in a vector database*********************"""
import chromadb
chroma_client = chromadb.PersistentClient()

collection = chroma_client.get_or_create_collection(name="RAG_demo_collection")

collection.add(embeddings=embeddings, ids=ids, documents=documents)

query = "Which animals are found in the Savanna?"
query_embeddings = embedding_fn([query])

results = collection.query(
    query_embeddings=query_embeddings,
    n_results=3,
)


##################################STEP 4##################################
"""********************Convert the queried results into a proper response using LLM*********************"""
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# Build the context block from your retrieved Chroma documents
context = "\n".join(results["documents"][0])  # Assuming you've already run collection.query()

prompt = f"""You are a knowledgeable assistant. Use the following context to answer the question.
            Context: {context}
            Question: {query}
            Answer:"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print(response.text)
