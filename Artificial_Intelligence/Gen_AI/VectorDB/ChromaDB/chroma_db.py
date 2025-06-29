#install Chroma DB
#pip install Chroma DB

#install sentence_transformers

#import the library
import chromadb
from chromadb.utils import embedding_functions                          #Change embedding settings
from datetime import datetime

sentence_transformer = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

"""
Imagine the client as a Database and the collections as tables
"""
#create a Chroma DB client and save it to path
chroma_client = chromadb.PersistentClient(path="Chroma_Database")

#Create a Chroma DB client in Memory (RAM)
#chroma_client = chromadb.EphemeralClient()

#Create a collection in the database
collection = chroma_client.create_collection(name="my_collection",
                                             embedding_function=sentence_transformer,
                                             metadata = {
                                                        "description": "my first Chroma collection",
                                                        "created": str(datetime.now())
                                             }
                                             )

peek = collection.peek() #returns the first 10 items of the collection
count = collection.count() #returns the number of items in the collection
collection.modify("new_name") #rename the collection
collection.modify("my_collection")

collection.add(
                documents=[
                    "This is a document about pineapple",
                    "This is a document about oranges"
                ],
                ids=["id1", "id2"],

              )

#get the list of in the Database
collection_list = chroma_client.list_collections()

#Delete a collection from teh database
#chroma_client.delete_collection(name="my_collection")

#get a collection
"""
collection = chroma_client.get_collection(name="test") # Get a collection object from an existing collection, by name. Will raise an exception if it's not found.
"""
#get a collection, create one if does not exist
"""
collection = chroma_client.get_or_create_collection(name="test") # Get a collection object from an existing collection, by name. If it doesn't exist, create it.
"""
results = collection.query(
    query_texts=["This is a query document about hawaii"], # Chroma will embed this for you
    n_results=2                                            # how many results to return, default value = 10
)

#returns a nanosecond heartbeat. Useful for making sure the client remains connected.
#chroma_client.heartbeat()

#empties and completely resets the database.
#chroma_client.reset()                                     #⚠️ This is destructive and not reversible.

