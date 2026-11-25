from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate

#model=ChatOpenAI(model="gpt-6-luna")

prompt=PromptTemplate.from_template("Translate the word {word} into {language}.")
print(prompt.invoke({"word":"Apple","language":"Spanish"}))