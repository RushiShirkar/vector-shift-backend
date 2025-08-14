from typing import List, Optional
from pydantic import BaseModel

class Node(BaseModel):
    id: str

class Edge(BaseModel):
    source: str
    target: str

class PipelinePayload(BaseModel):
    nodes: List[Node]
    edges: List[Edge]

class PipelineStats(BaseModel):
    num_nodes: int
    num_edges: int
    is_dag: bool