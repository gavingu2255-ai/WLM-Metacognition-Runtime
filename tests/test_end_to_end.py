# test_end_to_end.py
```python
from wlm_metacognition_runtime import analyze_reasoning


def test_end_to_end_pipeline_runs():
    result = analyze_reasoning("If A then B.")
    assert isinstance(result, dict)
    assert "steps" in result
    assert "consistency" in result
    assert "dimensions" in result
    assert "signals" in result
    assert "metacognitive_graph" in result
```

