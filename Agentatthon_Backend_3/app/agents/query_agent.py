from app.agents.base import BaseAgent
from app.agents.result import AgentResult

class QueryAgent(BaseAgent):
    name = "query_agent"

    async def run(self, query: str) -> AgentResult:
        query = query.strip()

        if len(query) < 5:
            return AgentResult(
                output=None,
                confidence=0.2,
                should_continue=False,
                notes="Query too vague"
            )

        return AgentResult(
            output=query,
            confidence=0.9,
            should_continue=True,
            notes="Query accepted"
        )
