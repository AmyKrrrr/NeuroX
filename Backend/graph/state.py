# app/graph/state.py
from typing import TypedDict, List, Optional, Any

class GraphState(TypedDict, total=False):
    query: str
    urls: List[str]
    documents: List[str]
    summaries: List[str]
    bias_scores: List[Any]
    final_report: str
    output: str