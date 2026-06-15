# QuickMath

Simple math CLI tool written in Python.

## Installation

```bash
pip install quickmath
```

## Usage

### As CLI
```bash
quickmath add 5 3      # → Result: 8.0
quickmath sub 10 4     # → Result: 6.0
quickmath mul 3 4      # → Result: 12.0
quickmath div 10 2     # → Result: 5.0
```

### As Library
```python
from quickmath import add, multiply

print(add(2, 3))       # 5
print(multiply(4, 5))  # 20
```

## License

Apache-2.0 — see [LICENSE](./LICENSE)

Copyright 2026 Sadia Khatun