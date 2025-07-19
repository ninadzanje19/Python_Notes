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
from constants import gemini_api_key
from langchain_google_genai import ChatGoogleGenerativeAI
llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.0-flash",
                                    api_key=gemini_api_key)


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