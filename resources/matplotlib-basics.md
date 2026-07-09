# Matplotlib Basics

Matplotlib creates charts from Python data.

## Install

```bash
python3 -m pip install matplotlib
```

## Simple Line Chart

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar"]
sales = [12000, 15000, 13500]

plt.plot(months, sales, label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.close()
```

Always add a title, labels, and `plt.tight_layout()`. Save each required chart using the exact file name from the question.
