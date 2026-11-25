from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
    model="gpt-6-luna",
    max_tokens=200
)

response = model.invoke("Hello, tell me history about the USA")
print(response.content)
print(response.response_metadata)
print(response.usage_metadata)