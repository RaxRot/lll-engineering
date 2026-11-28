from langchain_core.messages import HumanMessage

#userMessage=HumanMessage(content="Write a little poem about a cat.")

prompt=[
    ("system","You are a helpful assistant.Always answer in {language}"),
    ("user","{text}")
]