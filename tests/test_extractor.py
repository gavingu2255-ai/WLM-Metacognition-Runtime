# test_extractor.py
```python
from wlm_metacognition_runtime.reasoning_extractor import extract_reasoning_trace


def test_extract_reasoning_trace_returns_list():
    result = extract_reasoning_trace("Some reasoning text.")
    assert isinstance(result, list)
```
