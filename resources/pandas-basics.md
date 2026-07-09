# Pandas Basics

Pandas helps you work with tabular data using a DataFrame.

## Install

```bash
python3 -m pip install pandas
```

## Start

```python
import pandas as pd

data = {"name": ["Aman", "Priya"], "marks": [85, 90]}
df = pd.DataFrame(data)
print(df)
```

## Useful Operations

```python
df["revenue"] = df["price"] * df["quantity"]
print(df[df["city"] == "Gorakhpur"])
print(df.groupby("category")["revenue"].sum())
```

Use clear column names, inspect data before calculations, and check your printed results against the assignment's expected values.
