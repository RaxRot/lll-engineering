from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-6-luna")

prompt="What is Python? Answer in two sentences."

for chunk in model.stream(prompt):
    print(chunk.content,end="",flush=True)