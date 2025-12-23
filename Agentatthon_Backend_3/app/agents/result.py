from pydantic import BaseModel
from typing import Any, Optional

class AgentResult(BaseModel):
    output: Any
    confidence: float = 0.5
    should_continue: bool = True
    notes: Optional[str] = None
