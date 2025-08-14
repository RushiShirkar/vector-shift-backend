from typing import Dict, List, Set
import time
from app.pipeline_schema import PipelinePayload, PipelineStats

def _has_cycle(graph: Dict[str, List[str]]) -> bool:
    WHITE, GRAY, BLACK = 0, 1, 2
    color: Dict[str, int] = {node: WHITE for node in graph}
    print(color)

    def dfs(node: str) -> bool:
        if color[node] == GRAY:
            return True
        if color[node] == BLACK:
            return False
        color[node] = GRAY
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True
        color[node] = BLACK
        return False

    for node in graph:
        if color[node] == WHITE and dfs(node):
            return True
    return False

def compute_pipeline_stats(payload: PipelinePayload) -> PipelineStats:
    node_ids = {n.id for n in payload.nodes}
    for e in payload.edges:
        node_ids.add(e.source)
        node_ids.add(e.target)

    graph: Dict[str, List[str]] = {n: [] for n in node_ids}
    for e in payload.edges:
        if e.source and e.target:
            graph[e.source].append(e.target)

    is_dag = not _has_cycle(graph)

    # Intentional delay before responding
    time.sleep(1)

    return PipelineStats(
        num_nodes=len(node_ids),
        num_edges=len(payload.edges),
        is_dag=is_dag,
    )