# NumPy Basics

NumPy is a Python library for fast numerical calculations with arrays.

## Install

```bash
python3 -m pip install numpy
```

## Start

```python
import numpy as np

marks = np.array([85, 90, 78, 92, 88])
print(marks)
print(marks.mean())
```

## Useful Operations

```python
print(marks.shape)
print(marks.size)
print(marks.sum())
print(marks.max())
print(marks[marks >= 90])
```

Use NumPy arrays when working with numbers, matrices, filtering, and repeated calculations.
