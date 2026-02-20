# WLM‑Metacognition‑Runtime — Overview

The **WLM‑Metacognition‑Runtime** is the execution layer for the WLM metacognition protocol.  
It provides the minimal runtime components required to support:

- reasoning‑trace extraction  
- structured reasoning‑step normalization  
- contradiction and consistency detection  
- dimension‑shift tracking  
- metacognitive signal generation  
- metacognitive graph assembly  

This runtime is intentionally minimal.  
It is designed to be extended or replaced by downstream systems.

---

## Purpose

The runtime provides:

- a clean Python package  
- stable module boundaries  
- placeholder implementations  
- consistent API surface  
- testable interfaces  
- documentation scaffolding  

It does **not** implement the full metacognition logic.  
That logic is defined in the **WLM‑Metacognition‑Engine** (protocol layer).

---

## Position in the WLM Stack

```
Structure → Reasoning → Self‑Monitoring → Stability
```

This runtime corresponds to the **sixth layer** of the WLM protocol stack.

---

## Key Modules

- `reasoning_extractor` — extract implicit reasoning traces  
- `consistency_engine` — detect contradictions  
- `dimension_tracker` — track dimension shifts  
- `signal_engine` — generate metacognitive signals  
- `graph_builder` — assemble the metacognitive graph  

---

## Status

- Runtime skeleton: complete  
- Placeholder logic: complete  
- Ready for extension: yes  
