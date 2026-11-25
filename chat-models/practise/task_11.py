from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate

model=ChatOpenAI(model="gpt-6-luna")

messages=[
    ("system","Ты преподаватель Python, который объясняет материал в зависимости от {level} ученика. Всегда отвечай на {language} языке"),
    ("user","Our topic is- {topic} and we need 1 small example of code")
]

my_prompt=ChatPromptTemplate(messages)
prompt=my_prompt.invoke({
    "topic":"Python dictionaries",
    "level":"Beginner",
    "language":"Russian"
})

response=model.invoke(prompt)
print(response.content)