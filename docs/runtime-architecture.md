# Runtime Architecture

The **WLM‑Metacognition‑Runtime** is organized into five core modules, each responsible for a distinct stage of the metacognitive pipeline.

```
Input Text
    ↓
Reasoning Trace Extraction
    ↓
Step Normalization
    ↓
Consistency Analysis
    ↓
Dimension Tracking
    ↓
Signal Generation
    ↓
Metacognitive Graph Assembly
```

---

## Module Breakdown

### 1. `reasoning_extractor`
Extracts implicit reasoning traces from raw text.  
MVP implementation returns an empty list.

### 2. `consistency_engine`
Analyzes reasoning steps for:

- contradictions  
- invalid transitions  
- unstable loops  

### 3. `dimension_tracker`
Tracks active reasoning dimensions:

- spatial  
- temporal  
- causal  
- physical  
- identity  
- knowledge  

### 4. `signal_engine`
Generates metacognitive signals:

- confidence  
- uncertainty  
- contradiction alerts  
- missing‑information flags  
- reasoning‑depth indicators  

### 5. `graph_builder`
Assembles the final metacognitive graph.

---

## Orchestration Flow

The `analyze_reasoning()` API coordinates all modules:

```
trace = extract_reasoning_trace(text)
consistency = analyze_consistency(trace)
dimensions = track_dimensions(trace)
signals = generate_signals(trace, consistency, dimensions)
graph = build_metacognitive_graph(...)
```

---

## Design Principles

- **Minimal** — only the runtime skeleton  
- **Deterministic** — same input → same structure  
- **Composable** — modules can be replaced independently  
- **Transparent** — all steps are inspectable  
- **Extensible** — downstream systems can plug in real logic  
