# api.py
```python
"""
Public API for WLM‑Metacognition‑Runtime.
"""

from .reasoning_extractor import extract_reasoning_trace
from .consistency_engine import analyze_consistency
from .dimension_tracker import track_dimensions
from .signal_engine import generate_signals
from .graph_builder import build_metacognitive_graph


def analyze_reasoning(text: str) -> dict:
    """
    Orchestrate the full metacognition runtime pipeline.
    """
    trace = extract_reasoning_trace(text)
    consistency = analyze_consistency(trace)
    dimensions = track_dimensions(trace)
    signals = generate_signals(trace, consistency, dimensions)
    graph = build_metacognitive_graph(
        trace=trace,
        consistency=consistency,
        dimensions=dimensions,
        signals=signals,
    )

    return {
        "steps": trace,
        "consistency": consistency,
        "dimensions": dimensions,
        "signals": signals,
        "metacognitive_graph": graph,
    }
```
