from openai import OpenAI
from constants import open_ai_api_key

client = OpenAI(api_key=open_ai_api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",  # Replace with the model you want
    messages=[
        {"role": "user", "content": "Tell me about AI in 5 sentences."}
    ]
)

print(response.choices[0].message.content)
