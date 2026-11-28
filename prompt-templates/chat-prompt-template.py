from langchain_core.prompts import ChatPromptTemplate

messages=[
    ("system","You are a helpful assistant."),
    ("user","Who is the president of {country1}?"),
    ("assistant","{answer}"),
    ("user","Who is the president of {country2}?")
]

chat_prompt_template=ChatPromptTemplate(messages)
chat_prompt=chat_prompt_template.invoke({
    "country1":"USA",
    "answer":"Elon Musk",
    "country2":"India"
})
print(chat_prompt)