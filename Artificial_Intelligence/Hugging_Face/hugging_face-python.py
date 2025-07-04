"""
pip install langchain
pip install langchain-huggingface
pip install transformers
In cmd write huggingface-cli login and paste your huggingface token
"""

from transformers import pipeline
import torch

print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))

model = pipeline("summarization", model="facebook/bart-large-cnn", device="0")
response = model("text to summarize")
print(response)