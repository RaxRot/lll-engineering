from langchain_core.prompts import PromptTemplate

prompt_template=PromptTemplate.from_template("Who is the {role} of {country}?")

print(prompt_template.template)
print(prompt_template.template_format)
print(prompt_template.input_variables)
print(prompt_template.validate_template)