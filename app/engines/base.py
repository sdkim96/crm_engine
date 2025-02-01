from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

from app.utils.tool import (
    add, 
    multiply, 
    tavily
)
from app.utils.constants import GPT_4O_MINI

openai = ChatOpenAI(model=GPT_4O_MINI)

# Tools
calculators = [add, multiply]
web_searcher = [tavily]

## LLM with Tools
openai_with_calculator = openai.bind_tools(calculators, tool_choice="auto")
openai_with_tavily = openai.bind_tools(web_searcher, tool_choice="auto")
