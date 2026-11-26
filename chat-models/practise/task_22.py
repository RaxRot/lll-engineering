from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.globals import set_llm_cache
from langchain_core.caches import InMemoryCache

set_llm_cache(InMemoryCache())

model=ChatOpenAI(model="gpt-6-luna")

prompt="Tell me one interesting fact about Python."

response1=model.invoke(prompt)
print(response1.content)
response2=model.invoke(prompt)
print(response2.content)