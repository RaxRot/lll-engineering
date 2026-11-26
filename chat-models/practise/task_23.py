from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.globals import set_llm_cache
from langchain_community.cache import SQLiteCache

set_llm_cache(SQLiteCache(database_path="practice_cache.db"))

model=ChatOpenAI(model="gpt-6-luna")

prompt="What is LangGraph? Answer in one sentence."

response1=model.invoke(prompt)
print(response1.content)
response2=model.invoke(prompt)
print(response2.content)