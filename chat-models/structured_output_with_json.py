from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-6-luna")

president_schema={
    "name":"president_info_schema",
    "description":"Gets infro about the president",
    "parameters":{
        "type":"object",
        "properties":{
           "name":{
               "type":"string",
               "description":"The name of the president"
           },
            "country":{
                "type":"string",
                "description":"The country of the president"
            },
            "age":{
                "type":"integer",
                "description":"The age of the president"
            }
        },
        "required":["name","country","age"]
    }
}

structured_output=model.with_structured_output(president_schema)
response=structured_output.invoke("Who is the president of USA?")
print(response)