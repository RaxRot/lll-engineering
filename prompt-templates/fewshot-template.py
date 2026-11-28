from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate

example_formatter=PromptTemplate.from_template("Question: {question} {answer}")

example_set = [
    {
        "question": "Tell me about US",
        "answer": "Continent: North America | Capital: Washington D.C.|President: Donald Trump| Language: English"
    },
    {
        "question": "Tell me about Spain",
        "answer": "Continent: Europe | Capital: Madrid | President: Pepe | Language: Spanish"
    }
]

few_shot_prompt_template = FewShotPromptTemplate(example_prompt=example_formatter,
                                                 examples=example_set,
                                                 suffix="Question: {user_query}")

invoked_template = few_shot_prompt_template.invoke({
    "user_query": "Tell me about Belarus"
})

print(invoked_template)
