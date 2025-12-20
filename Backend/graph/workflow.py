# app/graph/workflow.py
from langgraph.graph import StateGraph, END

from app.graph.state import GraphState

from app.nodes.search import search_node
from app.nodes.scrape import scrape_node
from app.nodes.bias import bias_node
from app.nodes.rewrite import rewrite_node
from app.nodes.final import final_node


def build_workflow():
    """
    Builds and compiles the LangGraph workflow
    """
    graph = StateGraph(GraphState)

    # Register nodes
    graph.add_node("search", search_node)
    graph.add_node("scrape", scrape_node)
    graph.add_node("bias", bias_node)
    graph.add_node("rewrite", rewrite_node)
    graph.add_node("final", final_node)

    # Entry point
    graph.set_entry_point("search")

    # Edges (optimized flow)
    graph.add_edge("search", "scrape")
    graph.add_edge("scrape", "bias")
    graph.add_edge("bias", "rewrite")
    graph.add_edge("rewrite", "final")
    graph.add_edge("final", END)

    return graph.compile()
