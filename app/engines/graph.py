from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition

from app.engines import nodes
from app.engines.models import State

from app.engines.nodes import tool_node

class Graph(StateGraph):

    def __init__(self):

        self._builder: StateGraph = StateGraph(State)
        self._builder.add_node("chatbot", nodes.chatbot)
        self._builder.add_node("tools", tool_node)


        self._builder.add_edge(START, "chatbot")
        self._builder.add_conditional_edges(
            "chatbot",
            tools_condition,
        )

        self._builder.add_edge("tools", "chatbot")
        self.graph = self._builder.compile()

graph = Graph().graph