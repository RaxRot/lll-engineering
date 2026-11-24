from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

model=ChatOpenAI(model="gpt-6-luna")
response=model.invoke("What is the capital of Portugal?")
print(response.content)