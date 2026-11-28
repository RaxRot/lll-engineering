from langchain_core.prompts import ChatPromptTemplate,FewShotChatMessagePromptTemplate
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-6-luna")

example_formatter = ChatPromptTemplate.from_messages([
    ("user", "{input}"),
    ("ai", "{output}")
])

example_set = [
    {
        "input": "2 plus 2",
        "output": "4"
    },
    {
        "input": "3 plus 3",
        "output": "6"
    }
]

few_shot_template=FewShotChatMessagePromptTemplate(example_prompt=example_formatter, examples=example_set)

main_prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant."),
    few_shot_template,
    ("user","{user_input}")
])

invoked_prompt=main_prompt.invoke({"user_input":"What is 2 plus 2?"})

response = model.invoke(invoked_prompt)
print(response.content)
