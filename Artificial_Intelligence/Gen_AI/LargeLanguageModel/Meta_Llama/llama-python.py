from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3")

prompt = input("Enter your prompt\n")

result = model.invoke(input=prompt)

print(result)