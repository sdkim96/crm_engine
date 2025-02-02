from langgraph.graph import StateGraph, START, END

from app.engines.eval_smartwork import nodes, models

class EvaluateSmartWorkGraph:
    def __init__(self):
        self._builder: StateGraph = StateGraph(models.EvalSmartWorkState)

        self._builder.add_node("analyze_bookmarks", nodes.analyze_bookmarks)
        self._builder.add_node("analyze_human", nodes.analyze_human)
        self._builder.add_node("calculate_smartwork_score", nodes.calculate_smartwork_score)

        self._builder.add_edge(START, "analyze_bookmarks")
        self._builder.add_edge("analyze_bookmarks", "analyze_human")
        self._builder.add_edge("analyze_human", "calculate_smartwork_score")
        self._builder.add_edge("calculate_smartwork_score", END)

        self.graph = self._builder.compile()

eval_smartwork = EvaluateSmartWorkGraph().graph