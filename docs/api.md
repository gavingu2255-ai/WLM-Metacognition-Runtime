# API Reference

This document describes the public API of the **WLM‑Metacognition‑Runtime**.

---

# `analyze_reasoning(text: str) → dict`

```python
def analyze_reasoning(text: str) -> dict:
    """
    Analyze reasoning structure and produce metacognitive signals.
    """
```

## Description

Runs the full metacognition pipeline:

1. Extract reasoning trace  
2. Normalize steps  
3. Analyze consistency  
4. Track dimensions  
5. Generate signals  
6. Build metacognitive graph  

---

## Return Format (MVP)

```json
{
  "steps": [],
  "consistency": [],
  "dimensions": {},
  "signals": [],
  "metacognitive_graph": {}
}
```

---

# Internal Modules

These modules are not part of the public API but are stable entry points for extension.

### `extract_reasoning_trace(text: str) → list`
Extract implicit reasoning steps.

### `analyze_consistency(trace: list) → list`
Detect contradictions and invalid transitions.

### `track_dimensions(trace: list) → dict`
Track active reasoning dimensions.

### `generate_signals(trace, consistency, dimensions) → list`
Generate metacognitive signals.

### `build_metacognitive_graph(...) → dict`
Assemble the final graph.
