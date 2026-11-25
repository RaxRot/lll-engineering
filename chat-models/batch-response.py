from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-6-luna")

prompts=["Who is the president of USA?","Who is the president of France?","Who is the president of Germany?"]

batch_responses=model.batch(prompts)

for response in batch_responses:
    print(response.content)