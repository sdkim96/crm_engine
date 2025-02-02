from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition

from app.engines.chatbot import nodes
from app.engines.chatbot.state import BasicChatbotState

class ChatBot(StateGraph):

    def __init__(self):

        self._builder: StateGraph = StateGraph(BasicChatbotState)
        self._builder.add_node("chatbot", nodes.chatbot)
        self._builder.add_node("tools", nodes.web_searcher)


        self._builder.add_edge(START, "chatbot")
        self._builder.add_conditional_edges(
            "chatbot",
            tools_condition,
        )

        self._builder.add_edge("tools", "chatbot")
        self.graph = self._builder.compile()

chatbot = ChatBot().graph