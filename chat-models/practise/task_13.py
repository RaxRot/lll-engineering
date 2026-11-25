from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate

model=ChatOpenAI(model="gpt-6-luna")

messages=[
    ("system","Always answer in {language} with this level {level}"),
    ("user","Give me {count} ideas for a {interest}")
]

my_prompt=ChatPromptTemplate(messages)
prompt=my_prompt.invoke({
    "language":"Russian",
    "level":"Beginner",
    "count":"3",
    "interest":"Artificial Intelligence"
})

response=model.invoke(prompt)
print(response.content)