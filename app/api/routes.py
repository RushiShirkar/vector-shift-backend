from fastapi import APIRouter
from app.schemas.pipeline import PipelinePayload, PipelineStats
from app.services.pipeline_service import compute_pipeline_stats

router = APIRouter(prefix="/pipelines", tags=["pipelines"])

@router.post("/parse", response_model=PipelineStats)
def parse_pipeline(payload: PipelinePayload) -> PipelineStats:
    return compute_pipeline_stats(payload)