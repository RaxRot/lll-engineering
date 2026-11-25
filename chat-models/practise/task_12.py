from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate,PromptTemplate

model=ChatOpenAI(model="gpt-6-luna")

my_prompt=PromptTemplate.from_template("Name three famous landmarks in {country}.")
prompt=my_prompt.invoke({"country":"Italy"})
response=model.invoke(prompt)
print(response.content)

messages=[
    ("system","Always reply in {langauge}"),
    ("user","Name three famous dish in {country}.")]

my_prompt=ChatPromptTemplate(messages)
prompt=my_prompt.invoke({
    "langauge":"Russian",
    "country":"Japan"
})
response=model.invoke(prompt)
print(response.content)