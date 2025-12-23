from abc import ABC, abstractmethod
from app.agents.result import AgentResult

class BaseAgent(ABC):
    name: str = "base"

    @abstractmethod
    async def run(self, *args, **kwargs) -> AgentResult:
        pass
