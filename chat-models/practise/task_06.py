from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate

#model=ChatOpenAI(model="gpt-6-luna")

prompt=PromptTemplate.from_template("Write a short poem about {animal} in {language}.")
print(prompt.format(animal="Cat",language="English"))