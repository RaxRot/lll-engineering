from langchain_core.prompts import PromptTemplate

string_prompt1=PromptTemplate(template="Write a poem about {topic}",input_variables=["topic"])
actual_prompt1=string_prompt1.invoke({"topic":"Dogs"})
print(actual_prompt1)

#recommended
string_prompt2=PromptTemplate.from_template("Write a poem about {animal}")
actual_prompt2=string_prompt2.invoke({"animal":"Cat"})
print(actual_prompt2)
