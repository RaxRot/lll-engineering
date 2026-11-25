from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-6-luna")

questions=[
    "What is the capital of Germany?",
    "What is the capital of Italy?",
    "What is the capital of Spain?"
]

responses=model.batch(questions)

for response in responses:
    print(response.content)