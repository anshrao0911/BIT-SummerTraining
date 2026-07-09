# Seaborn Basics

Seaborn builds attractive statistical charts from Pandas DataFrames.

## Install

```bash
python3 -m pip install pandas seaborn matplotlib
```

## Start

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
```

## Common Charts

```python
sns.countplot(data=df, x="course")
sns.barplot(data=df, x="course", y="marks")
sns.scatterplot(data=df, x="study_hours", y="marks", hue="course")
sns.boxplot(data=df, x="course", y="marks")
```

For a correlation heatmap:

```python
numeric_data = df[["study_hours", "marks", "attendance"]]
sns.heatmap(numeric_data.corr(), annot=True)
```

Use `plt.title()`, `plt.tight_layout()`, `plt.savefig()`, and `plt.close()` for every chart.
