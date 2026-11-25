from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-6-luna")

system_message=SystemMessage(content="You are a helpful assistant.Always answer in Spanish.")
user_message=HumanMessage(content="Who is the president of USA?")

response=model.invoke([
    system_message,
    user_message
])
print(response.content)