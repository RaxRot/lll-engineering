from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage,SystemMessage

model=ChatOpenAI(model="gpt-6-luna")

system_message=SystemMessage(content="You are a helpful assistant. Always answer in Russian.")
human_message=HumanMessage(content="What is the capital of Canada?")

response=model.invoke([
    system_message,
    human_message
])
print(response.content)