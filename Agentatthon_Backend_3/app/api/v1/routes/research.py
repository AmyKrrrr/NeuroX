from fastapi import APIRouter
from app.schemas.research import ResearchRequest
from app.services.orchestrator import run_research_pipeline

router = APIRouter()

@router.post("/research")
async def research(request: ResearchRequest):
    result = await run_research_pipeline(request.query)
    return result
