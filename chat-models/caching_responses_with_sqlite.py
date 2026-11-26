from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.globals import set_llm_cache
from langchain_community.cache import SQLiteCache

model=ChatOpenAI(model="gpt-6-luna")

set_llm_cache(SQLiteCache(database_path="my_cached_responses.db"))

prompt="Tell me a joke."

response1=model.invoke(prompt)
print(response1.content)
response2=model.invoke(prompt)
print(response2.content)