from langchain_core.prompts import PromptTemplate

prompt_template=PromptTemplate.from_template("Who is the {role} of {country}?")

invoked_prompt=prompt_template.invoke({
    "role":"president",
    "country":"USA"
})

formatted_prompt=prompt_template.format(role="president", country="USA")


formatted_prompt2=prompt_template.format_prompt(role="president", country="USA")

batched_prompt=prompt_template.batch([
    {"role":"president","country":"USA"},
    {"role":"Leader","country":"India"}
])



print(invoked_prompt)
print(formatted_prompt)
print(formatted_prompt2)
print(batched_prompt)

prompt_template.pretty_print()

prompt_template.save("my_prompt_template.json")