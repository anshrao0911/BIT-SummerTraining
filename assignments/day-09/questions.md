# Day 9 Assignment

## Topic: Pandas Data Analysis

Complete all questions in one file named `solution.py`.

Use Pandas for this assignment. Do not use Matplotlib or Seaborn yet.

Install Pandas if required:

```bash
python3 -m pip install pandas
```

Start your program with:

```python
import pandas as pd
```

Use this data to create a DataFrame:

```python
sales_data = {
    "product": ["Python Course", "Data Analytics Course", "AI Workshop", "Python Course", "Data Analytics Course", "AI Workshop"],
    "category": ["Online Course", "Online Course", "Workshop", "Online Course", "Online Course", "Workshop"],
    "price": [999, 1499, 799, 999, 1499, 799],
    "quantity": [2, 1, 3, 1, 2, 1],
    "city": ["Gorakhpur", "Lucknow", "Gorakhpur", "Deoria", "Gorakhpur", "Lucknow"]
}
```

## Questions

### Question 1: Create and Print a DataFrame

Create a DataFrame named `df` from `sales_data`. Print the DataFrame.

### Question 2: Inspect the Data

Print the number of rows and columns in this format:

```python
# Expected Output:
# Rows: 6
# Columns: 5
```

### Question 3: Add Revenue Column

Create a `revenue` column using `price * quantity`. Print only the `product` and `revenue` columns.

### Question 4: Total Revenue

Calculate and print the total revenue.

```python
# Expected Output:
# Total revenue: 10690
```

### Question 5: Filter Gorakhpur Sales

Create a new DataFrame containing rows where the city is `Gorakhpur`. Print its `product`, `quantity`, and `revenue` columns.

### Question 6: Revenue by Category

Use `groupby` to calculate and print total revenue by category.

```python
# Expected Values:
# Online Course: 7494
# Workshop: 3196
```

### Question 7: Revenue by City

Use `groupby` to calculate and print total revenue by city.

```python
# Expected Values:
# Deoria: 999
# Gorakhpur: 7393
# Lucknow: 2298
```

### Question 8: Top Revenue Product

Group the data by product, find the product with the highest total revenue, and print it.

```python
# Expected Output:
# Top product: Data Analytics Course
```

## Submission

Create your solution here:

```txt
assignments/day-09/submissions/batch-a/your-name/solution.py
```

or

```txt
assignments/day-09/submissions/batch-b/your-name/solution.py
```
