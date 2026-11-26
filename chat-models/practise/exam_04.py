from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.globals import set_llm_cache
from langchain_core.caches import InMemoryCache

from langchain_core.prompts import ChatPromptTemplate

set_llm_cache(InMemoryCache())

messages = [
    ("system", "You are python teacher!Reply briefly and understandable"),
    ("user", "{question}")
]

my_prompt=ChatPromptTemplate(messages)
prompt=my_prompt.invoke({
    "question":"What is a Python list?"
})

model=ChatOpenAI(model="gpt-6-luna")

response1=model.invoke(prompt)
print(response1.content)
response2=model.invoke(prompt)
print(response2.content)