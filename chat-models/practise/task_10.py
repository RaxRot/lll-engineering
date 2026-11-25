from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate

model=ChatOpenAI(model="gpt-6-luna")

messages=[
    ("system","You are a helpful assistant.Always translate answer in {language} and using {style} style. Give me back only the translated text."),
    ("user","{text}")
]

my_prompt=ChatPromptTemplate(messages)
prompt=my_prompt.invoke({
    "text":"I am learning Python and building AI applications.",
    "style":"Formal",
    "language":"Spanish"
})

response=model.invoke(prompt)
print(response.content)