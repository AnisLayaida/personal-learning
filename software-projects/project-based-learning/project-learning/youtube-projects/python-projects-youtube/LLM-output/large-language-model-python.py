from dotenv import load_dotenv
import os

import pandas as pd

from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List, Dict

load_dotenv()

api_key = os.environ['OPENAI_API_KEY']
model = ChatOpenAI(OPENAI_API_KEY=api_key, temperature=0)

# ----------- Define output data types within the class and initialize a parser ------------
class Fighters(BaseModel):

    values: list = Field(description="Python list of dictionaries containing UFC fighter name and nationality")
    country: str = Field(description="Give me the most popular country across the results")

parser = PydanticOutputParser(pydantic_object=Fighters)

print(parser.get_formatted_output())

# ----------- Set up the requests ----------------------------------------------------------
human_prompt = HumanMessagePromptTemplate.from_template("{request}\n{format_instructions}")
chat_prompt = ChatPromptTemplate.from_messages([human_prompt])

request = chat_prompt.format_prompt(
    request="Give me facts about  20 current UFC fighters",
    format_instructions=parser.get_format_instructions()
).to_messages()

results = model(request, temperature=0)
results_values = parser.parse(results.content)   # Player Class Object

# ----------- Show the results ----------------------------------------------------------
results_dataframe = pd.DataFrame.from_dict(results_values.values)

print(results_dataframe.head(10))
print(results_dataframe.shape)

print(f"The most popular country across the results is {results_dataframe['country']}")