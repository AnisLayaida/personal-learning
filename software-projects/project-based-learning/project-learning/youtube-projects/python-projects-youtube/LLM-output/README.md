# Get LLM output as Python object with Langchain and Pydantic

# Action Plan:

1. Define output datatypes -> Prepare OOP class and use PydanticOutputParser inside
2. Define a human prompt -> directly incorporate into chat prompt
3. Request -> Message we send to LLM model -> Uses parameters in PydanticOutputParser Class and the human prompt
4. Set up LLM Model with Langchain using OpenAI API
5. Output of LLM is the result, required info in a schema provided by the PydanticOutputParser
