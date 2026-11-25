from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate

model=ChatOpenAI(model="gpt-6-luna")

messages=[
    ("system","Always translate from {native_language} to {target_language} at {level} level."),
    ("user","{word}")
]

my_prompt=ChatPromptTemplate(messages)
prompt=my_prompt.invoke({
    "word":"Opportunity",
    "native_language":"English",
    "target_language":"Russian",
    "level":"Beginner"
})

response=model.invoke(prompt)
print(response.content)