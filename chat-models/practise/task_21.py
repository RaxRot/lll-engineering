from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-6-luna")

response=model.invoke("What is LangChain? Answer briefly.")
print(response.content)
print(response.usage_metadata)
print(response.usage_metadata["input_tokens"])
print(response.usage_metadata["output_tokens"])
print(response.usage_metadata["total_tokens"])