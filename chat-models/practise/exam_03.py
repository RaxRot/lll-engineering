from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-6-luna")

combined = None

for chunk in model.stream("Explain what an AI agent is in two sentences."):
    print(chunk.content,end="",flush=True)
    combined = chunk if combined is None else combined + chunk

print(combined.usage_metadata)