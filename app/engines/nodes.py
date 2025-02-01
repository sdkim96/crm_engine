from langgraph.prebuilt import ToolNode

from app.engines.base import (
    openai_with_tavily, 
    web_searcher
)
from app.engines.models import State


def chatbot(state: State):

    messages=[openai_with_tavily.invoke(state.messages)]
    state.messages = messages

    return state
    
tool_node = ToolNode(tools=web_searcher)