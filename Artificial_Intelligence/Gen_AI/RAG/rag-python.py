#Prepare Data – Split documents into small chunks.
#Store Data – Convert text into vectors and store in a database.
#Retrieve Information – Find the most relevant text when a user asks a question.
#Generate Response – Use an AI model to create a useful answer.
#Return Answer – Show the response to the user in a clean format.


"""from langchain.text_splitter import RecursiveCharacterTextSplitter

# Sample API documentation text
text =
The API has 2 endpoints. The first endpoint takes in the user data of name, age, city, and work.
The name should be of two words without any punctuation marks. The age should be a number greater than 0.
The city should be a real city or town. Once the data is given, a quotation ID is generated for the data given.

The second endpoint takes in the quotation ID and the data of the user and analyzes whether the user should be granted the policy or not.
If the age of the user is greater than 50, the policy is not granted. Also, if the work of the person is considered to be hazardous,
the policy is not granted to the user.


# Initialize the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,  # Max size of each chunk
    chunk_overlap=20  # Overlap to preserve context
)

# Split the text into chunks
chunks = text_splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n{'-'*50}")

from sentence_transformers import SentenceTransformer

# Load a pre-trained model for generating embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# Example documents (text chunks from your API documentation)
documents = [
    "The API has two endpoints.",
    "The first endpoint takes user data like name, age, city, and work.",
    "The second endpoint analyzes whether the user is eligible for a policy.",
    "If the age of the user is greater than 50, the policy is not granted."
]

# Convert documents into embeddings (vectors)
embeddings = model.encode(documents)
"""

##################################STEP 1##################################
"""********************Break your data into chunks*********************"""
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Your large text string
with open("document.txt", "r", encoding="utf-8") as doc_text:
    doc_text = doc_text.read()

# Create the splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,       # Customize depending on your model
    chunk_overlap=50      # Helps maintain context between chunks
)

# Create the chunks
chunks = text_splitter.create_documents([doc_text])

##################################STEP 2##################################
"""********************Convert the data chunks to vector embeddings*********************"""
from chromadb.utils import embedding_functions

#Configure the embedding function
embedding_fn = embedding_functions.DefaultEmbeddingFunction()

#Pass the embedding data chunks to the embedding function to create embeddings
embeddings = []
for chunk in chunks:
    embeddings.append(chunk.page_content)

embeddings = embedding_fn(embeddings)


#Generate unique ids for each embedding. {len(ids) == len(embeddings)}
import uuid
ids = []
for _ in range(len(embeddings)):
    ids.append(str(uuid.uuid4()))


##################################STEP 3##################################
"""********************Store the vector embeddings in a vector database*********************"""
import chromadb
chroma_client = chromadb.PersistentClient()

collection = chroma_client.create_collection(name="RAG_demo_collection")

collection.add(embeddings=embeddings, ids=ids)

query = "Which animals are found in the Savanna?"

results = collection.query(
    query_texts=[query],
    n_results=3,
    include=["documents"]
)
print(results)
# Print each result
for doc in results["documents"][0]:
    print(type(doc))



import google.generativeai as genai

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

# Join the retrieved chunks into a single block of context
context = "\n".join(results["documents"][0])

# Define the user question
query = "Which animals migrate in the Savanna?"

# Construct the prompt
prompt = f"""You are a helpful assistant. Use the following context to answer the question:

{context}

Question: {query}
Answer:"""

# Get the response from Gemini
response = model.generate_content(prompt)

# Print the final answer
print(response.text)
