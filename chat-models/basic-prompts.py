from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-6-luna")

prompt1=PromptTemplate(template="What is the capital of France")
#recommended
prompt2=PromptTemplate.from_template("What is the capital of {country}?")

#print(prompt1.format())

print(prompt2.invoke({
    "country":"France"
}))
print(prompt2.format(country="India"))

my_prompt=prompt2.invoke({"country":"India"})
response = model.invoke(my_prompt)
print(response.content)