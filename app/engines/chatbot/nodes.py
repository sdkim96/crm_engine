from langgraph.prebuilt import ToolNode

from app.engines.base import (
    openai_with_tavily, 
    web_searcher
)
from app.engines.chatbot.state import BasicChatbotState


def chatbot(state: BasicChatbotState):

    human_m = state.query
    state.messages.append(human_m)

    ai_m = openai_with_tavily.invoke(state.messages)
    state.messages.append(ai_m)

    return state
    
web_searcher = ToolNode(tools=web_searcher)


