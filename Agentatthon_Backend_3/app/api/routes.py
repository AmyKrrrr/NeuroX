from fastapi import APIRouter
from pydantic import BaseModel
from app.workflows.orchestrator import ResearchOrchestrator
from app.workflows.explainer import explain_trace

router = APIRouter()

class ResearchRequest(BaseModel):
    query: str

@router.post("/research")
async def research(req: ResearchRequest):
    orchestrator = ResearchOrchestrator()
    return await orchestrator.run(req.query)

@router.post("/research/explain")
async def research_with_explanation(req: ResearchRequest):
    orchestrator = ResearchOrchestrator()
    result = await orchestrator.run(req.query)

    if "trace" in result:
        result["explanation"] = explain_trace(result["trace"])

    return result
