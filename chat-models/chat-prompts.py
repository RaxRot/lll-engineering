from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-6-luna")

prompts=[
    ("system","You are a helpful assistant.Always answer in {language}"),
    ("user","Who is the president of {country}?")
]

my_prompt=ChatPromptTemplate(prompts)
chat_prompt=my_prompt.invoke({
    "language": "French",
    "country":"USA"
})

response=model.invoke(chat_prompt)
print(response.content)