# Day 7 Assignment

## Topic: CSV Data Analytics With Python

Complete all 8 questions using a file named `solution.py` and a data file named `sales_data.csv`.

Use Python's built-in `csv` module and `csv.DictReader`. Do not use Pandas, NumPy, or any external library.

Create `sales_data.csv` in your own submission folder with this exact content:

```csv
order_id,product,category,price,quantity,city
ORD-001,Python Course,Online Course,999,2,Gorakhpur
ORD-002,Data Analytics Course,Online Course,1499,1,Lucknow
ORD-003,AI Workshop,Workshop,799,3,Gorakhpur
ORD-004,Python Course,Online Course,999,1,Deoria
ORD-005,Data Analytics Course,Online Course,1499,2,Gorakhpur
ORD-006,AI Workshop,Workshop,799,1,Lucknow
```

Convert `price` and `quantity` to integers before calculating revenue.

## Basic Questions

### Question 1: Read the CSV File

Read all rows from `sales_data.csv` and print the total number of orders.

```python
# Expected Output:
# Total orders: 6
```

### Question 2: Total Units Sold

Calculate and print the total quantity sold.

```python
# Expected Output:
# Total units sold: 10
```

### Question 3: Total Revenue

Calculate and print the total revenue from the CSV data.

```python
# Expected Output:
# Total revenue: 10690
```

### Question 4: Average Order Revenue

Calculate total revenue divided by total orders. Round the result to 2 decimal places.

```python
# Expected Output:
# Average order revenue: 1781.67
```

## Medium Questions

### Question 5: Category Revenue Report

Create and print a dictionary of total revenue by category.

```python
# Expected Output:
# {'Online Course': 7494, 'Workshop': 3196}
```

### Question 6: City Revenue Report

Create and print a dictionary of total revenue by city.

```python
# Expected Output:
# {'Gorakhpur': 7393, 'Lucknow': 2298, 'Deoria': 999}
```

### Question 7: Top Product

Find the product with the highest total revenue and print it.

```python
# Expected Output:
# Top product: Data Analytics Course
```

### Question 8: Gorakhpur Orders

Create a list of `order_id` values where the city is `"Gorakhpur"`. Keep the CSV order and print the list.

```python
# Expected Output:
# Gorakhpur order IDs: ['ORD-001', 'ORD-003', 'ORD-005']
```

## Submission

Create both files inside your own folder:

```txt
assignments/day-07/submissions/batch-a/your-name/solution.py
assignments/day-07/submissions/batch-a/your-name/sales_data.csv
```

or

```txt
assignments/day-07/submissions/batch-b/your-name/solution.py
assignments/day-07/submissions/batch-b/your-name/sales_data.csv
```
