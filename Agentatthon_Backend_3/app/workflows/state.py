from pydantic import BaseModel
from typing import Dict, Any, List

class WorkflowState(BaseModel):
    query: str
    artifacts: Dict[str, Any] = {}
    trace: List[Dict[str, Any]] = []

    def record(self, agent: str, result):
        self.trace.append({
            "agent": agent,
            "confidence": result.confidence,
            "continued": result.should_continue,
            "notes": result.notes
        })
