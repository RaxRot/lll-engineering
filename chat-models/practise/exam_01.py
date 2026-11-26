from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate

model=ChatOpenAI(model="gpt-6-luna")

messages = [
    ("system", "You are a translator.Always answer in {language}"),
    ("user", "{text}")
]

my_prompt=ChatPromptTemplate(messages)
prompt=my_prompt.invoke({
    "text":"I love learning Python",
    "language":"German"
})

response=model.invoke(prompt)
print(response.content)
