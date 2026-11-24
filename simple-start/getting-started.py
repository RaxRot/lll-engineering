from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

model=ChatOpenAI(model="gpt-6-luna")

response=model.invoke("Where is the statue of Liberty?")
print(response.content)