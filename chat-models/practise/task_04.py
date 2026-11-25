from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate

#model=ChatOpenAI(model="gpt-6-luna")

prompt=PromptTemplate.from_template("What is the capital of {country}?")
print(prompt.invoke({"country":"Brazil"}))