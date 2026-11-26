from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-6-luna")

streamed_response=model.stream("Tell me about NBA.")
for chunk in streamed_response:
    print(chunk.content,end="",flush=True)