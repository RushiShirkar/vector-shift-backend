from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from app.pipeline_service import compute_pipeline_stats
from app.pipeline_schema import PipelinePayload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.post('/pipelines/parse')
def parse_pipeline(pipeline: PipelinePayload):
    return compute_pipeline_stats(pipeline)