from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition

from app.engines.eval_smartwork import nodes
from app.engines.eval_smartwork.models import EvalSmartWorkState

class EvaluateSmartWorkGraph:
    def __init__(self):
        self._builder: StateGraph = StateGraph(EvalSmartWorkState)
        self._builder.add_node("analyze_human", nodes.analyze_human)
        self._builder.add_node("calculate_smartwork_score", nodes.calculate_smartwork_score)

        self._builder.add_edge(START, "analyze_human")
        self._builder.add_edge("analyze_human", "calculate_smartwork_score")
        self._builder.add_edge("calculate_smartwork_score", END)

        self.graph = self._builder.compile()

eval_smartwork = EvaluateSmartWorkGraph().graph