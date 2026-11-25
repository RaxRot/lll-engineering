from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate

model=ChatOpenAI(model="gpt-6-luna")

messages=[
    ("system","You are a helpful assistant.Always answer in {language}"),
    ("user","What is the capital of {country}?")]

my_prompt=ChatPromptTemplate(messages)
prompt=my_prompt.invoke({
    "language": "Russian",
    "country":"Australia"
})

response=model.invoke(prompt)
print(response.content)