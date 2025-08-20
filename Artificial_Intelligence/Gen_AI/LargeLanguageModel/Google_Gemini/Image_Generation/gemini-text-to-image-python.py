from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64


from constants import gemini_api_key

client = genai.Client(api_key=gemini_api_key)

#Prompt for the image
contents = "Generate an image of an Elephant in an Indian Jungle"

response = client.models.generate_content(
    model="gemini-2.0-flash-preview-image-generation",
    contents=contents,
    config=types.GenerateContentConfig(
      response_modalities=['TEXT', 'IMAGE']
    )
)

#extract the image and save or show it
image = Image.open(BytesIO(response.candidates[0].content.parts[1].inline_data.data))
#    image.save('gemini-native-image.png')
image.show()