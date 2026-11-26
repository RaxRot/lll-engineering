from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

from langchain_community.callbacks.manager import get_openai_callback

model=ChatOpenAI(model="gpt-6-luna")

with get_openai_callback() as callback:
    response=model.invoke("Who is the president of the United States?")
    print(callback)