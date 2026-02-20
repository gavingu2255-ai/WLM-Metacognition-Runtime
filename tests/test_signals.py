# test_signals.py
```python
from wlm_metacognition_runtime.signal_engine import generate_signals


def test_generate_signals_returns_list():
    result = generate_signals([], [], {})
    assert isinstance(result, list)
```
