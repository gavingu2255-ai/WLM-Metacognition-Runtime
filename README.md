# WLM‑Metacognition‑Runtime  
**Runtime implementation for structured metacognition in WLM**

The **WLM‑Metacognition‑Runtime** is the engineering/runtime layer for the WLM metacognition protocol.  
It provides the minimal executable components required to support:

- reasoning‑trace extraction  
- structured reasoning‑step normalization  
- contradiction and consistency detection  
- dimension‑shift tracking  
- metacognitive signal generation  
- metacognitive graph assembly  

This repository implements the **runtime skeleton** for the sixth layer of WLM:

> **Structure → Reasoning → Self‑Monitoring → Stability**

This runtime is intentionally minimal and designed for extension.

---

# 📌 Purpose

This repository provides:

- a clean Python package  
- stable module boundaries  
- placeholder implementations  
- consistent API surface  
- testable interfaces  
- documentation scaffolding  

It does **not** implement the full metacognition logic.  
That logic is defined in the **WLM‑Metacognition‑Engine** (protocol layer).  
This runtime simply provides the **execution layer**.

---

# 🧱 Architecture

```
WLM‑Metacognition‑Engine   →   WLM‑Metacognition‑Runtime
(protocol / structure)         (runtime / execution)
```

Core runtime modules:

- `reasoning_extractor` — extract implicit reasoning traces  
- `consistency_engine` — detect contradictions  
- `dimension_tracker` — track dimension shifts  
- `signal_engine` — generate metacognitive signals  
- `graph_builder` — assemble the metacognitive graph  

---

# 🚀 Quickstart

## Install

```bash
pip install wlm-metacognition-runtime
```

## Use

```python
from wlm_metacognition_runtime import analyze_reasoning

result = analyze_reasoning("If Earth orbits the Sun, then seasons occur.")
print(result)
```

### Output (MVP placeholder)

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

# 🧩 API

### `analyze_reasoning(text: str) → dict`

```python
def analyze_reasoning(text: str) -> dict:
    """
    Analyze reasoning structure and produce metacognitive signals.
    """
```

This function orchestrates:

1. reasoning extraction  
2. step normalization  
3. consistency analysis  
4. dimension tracking  
5. signal generation  
6. graph assembly  

---

# 📁 Repository Structure

```
WLM-Metacognition-Runtime/
│
├── LICENSE
├── README.md
├── pyproject.toml
├── setup.cfg
│
├── src/
│   └── wlm_metacognition_runtime/
│       ├── __init__.py
│       ├── api.py
│       ├── reasoning_extractor.py
│       ├── consistency_engine.py
│       ├── dimension_tracker.py
│       ├── signal_engine.py
│       ├── graph_builder.py
│       └── utils.py
│
├── docs/
│   ├── overview.md
│   ├── runtime-architecture.md
│   ├── api.md
│   └── roadmap.md
│
└── examples/
    ├── simple_reasoning.py
    ├── contradiction.py
    └── dimension_switch.py
```

---

# 🧬 Design Principles

- **Minimal** — only the runtime skeleton, no heavy logic  
- **Deterministic** — same input → same structure  
- **Composable** — each module can be replaced independently  
- **Transparent** — all steps are inspectable  
- **Extensible** — downstream systems can plug in real logic  

---

# 🛠 Status

- Runtime skeleton: **complete**  
- Placeholder implementations: **complete**  
- Ready for downstream extension: **yes**  
- Full metacognition logic: defined in `WLM‑Metacognition‑Engine`  

---

# 📜 License

MIT License © 2026 Wujie Gu

---

# 🧩 Summary

**WLM‑Metacognition‑Runtime** is the execution layer for WLM’s structured metacognition protocol.  
It provides the minimal, clean, extensible runtime needed to support:

- reasoning trace extraction  
- consistency checking  
- dimension tracking  
- metacognitive signal generation  
- metacognitive graph construction  

It is the foundation for **transparent, stable, self‑monitoring AI reasoning**.
