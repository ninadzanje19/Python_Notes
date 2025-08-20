from google import genai

from constants import gemini_api_key

#Initialize the Google Gemini Client as an object.
client = genai.Client(api_key = gemini_api_key)

########################################################################################################################
#                                   Simple Gemini Calling
########################################################################################################################
#Get the response by specifying the model and the prompt
simple_response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="How to make a cake?"
)

#Get the text from the response generated
response_text = simple_response.text

########################################################################################################################
#                                   System Instructions and Configurations
########################################################################################################################
from google.genai import types

instructed_response = client.models.generate_content(
    model="gemini-2.5-flash",
    #Configure the response
    config=types.GenerateContentConfig(
        system_instruction="You are a cat. Your name is Neko.",             #Instruct the response to be given by a specific entity
        temperature=0.7),                                                   #Configure the temperature between 0 and 2.0 to control the randomness
    contents="Hello there"
).text

########################################################################################################################
#                                   Multimodal Inputs
########################################################################################################################
import requests
import io
from PIL import Image

#Load the media
image = requests.get("https://static.vecteezy.com/system/resources/thumbnails/026/350/646/small/majestic-elephant-walking-in-tranquil-african-forest-generated-by-ai-free-photo.jpg").content
image = io.BytesIO(image)
image = Image.open(image)

#Pass the image as contents along with the prompt
multimodal_response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[image, "Describe this image"]
).text

########################################################################################################################
#                                   Chat using Gemini
########################################################################################################################
#Configure the client to chat
chat = client.chats.create(model="gemini-2.5-flash")

#Send to the chat
chat_response = chat.send_message("I have 2 dogs in my house.")
chat_response = chat.send_message("How many paws are in my house?")

#Get chat history
chat_history = chat.get_history()
########################################################################################################################
#                                   Structured Output
########################################################################################################################
#Get the output in a structured way
from pydantic import BaseModel

#Define the Pydantic class as a schema of the output
class StructuredResponse(BaseModel):
    ingredients: list[str]
    recipie: str

structured_response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="How to make a cake?",
    config={
        "response_mime_type": "application/json",                                                          #Configure the output as a json
        "response_schema": StructuredResponse,                                                             #Pass the class model
    },
).parsed

