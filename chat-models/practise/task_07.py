from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate

model=ChatOpenAI(model="gpt-6-luna")

prompt_template=PromptTemplate.from_template("What is the capital of {country}? Answer in {language}.")
prompt=prompt_template.invoke({
    "country":"Portugal",
    "language":"Russian"
})

response=model.invoke(prompt)
print(response.content)