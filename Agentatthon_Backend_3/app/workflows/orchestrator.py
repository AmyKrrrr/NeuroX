from app.workflows.state import WorkflowState
from app.workflows.policy import (
    RETRIEVAL_CONFIDENCE_THRESHOLD,
    MAX_RETRIEVAL_RETRIES
)
from app.agents.query_agent import QueryAgent
from app.agents.retrieval_agent import RetrievalAgent
from app.agents.synthesis_agent import SynthesisAgent

class ResearchOrchestrator:
    async def run(self, query: str):
        state = WorkflowState(query=query)

        q = QueryAgent()
        r = RetrievalAgent()
        s = SynthesisAgent()

        # ---- QUERY ----
        q_res = await q.run(query)
        state.record(q.name, q_res)
        if not q_res.should_continue:
            return {"error": q_res.notes, "trace": state.trace}

        # ---- RETRIEVAL (WITH RETRY) ----
        retries = 0
        r_res = None

        while retries <= MAX_RETRIEVAL_RETRIES:
            r_res = await r.run(q_res.output)
            state.record(r.name, r_res)

            if r_res.confidence >= RETRIEVAL_CONFIDENCE_THRESHOLD:
                break

            retries += 1

        if r_res.confidence < RETRIEVAL_CONFIDENCE_THRESHOLD:
            return {
                "error": "Insufficient retrieval confidence after retry",
                "trace": state.trace
            }

        # ---- SYNTHESIS ----
        s_res = await s.run(query, r_res.output)
        state.record(s.name, s_res)

        return {
            "query": query,
            "answer": s_res.output,
            "confidence": s_res.confidence,
            "trace": state.trace
        }
