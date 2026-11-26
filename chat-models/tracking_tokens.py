from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-6-luna")

response=model.invoke("Who is the president of Egypt?")
print(response.usage_metadata)
#print(response.response_metadata["token_usage"])