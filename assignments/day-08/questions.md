# Day 8 Assignment

## Topic: NumPy Fundamentals

Complete all questions in one file named `solution.py`.

Use the NumPy library only. Do not use Pandas, Matplotlib, or Seaborn in this assignment.

Install NumPy if required:

```bash
python3 -m pip install numpy
```

Start your program with:

```python
import numpy as np
```

## Questions

### Question 1: Create a NumPy Array

Create a one-dimensional NumPy array containing these marks and print it:

```python
[85, 90, 78, 92, 88]
```

### Question 2: Array Shape and Size

Print the shape and total number of elements in the array from Question 1.

```python
# Expected Output:
# Shape: (5,)
# Size: 5
```

### Question 3: Basic Calculations

Using the marks array, print the total, average, maximum, and minimum.

```python
# Expected Output:
# Total: 433
# Average: 86.6
# Maximum: 92
# Minimum: 78
```

### Question 4: Create a 2D Array

Create this 2D NumPy array and print it:

```python
[[10, 20, 30],
 [40, 50, 60]]
```

### Question 5: Indexing and Slicing

From the 2D array in Question 4, print the value `50` and then print the first row.

```python
# Expected Output:
# 50
# [10 20 30]
```

### Question 6: Element-Wise Operations

Create `numbers = np.array([1, 2, 3, 4, 5])`. Print the result of multiplying every element by 10.

```python
# Expected Output:
# [10 20 30 40 50]
```

### Question 7: Filter Values

Using the marks array, create and print a new array containing marks greater than or equal to 90.

```python
# Expected Output:
# [90 92]
```

### Question 8: Student Marks Matrix

Create this matrix, where each row represents Python, Data Analytics, and AI marks for one student:

```python
[[85, 78, 90],
 [92, 88, 95],
 [76, 82, 80]]
```

Print the average mark for each student using NumPy.

```python
# Expected Output:
# [84.33 91.67 79.33]
```

## Submission

Create your solution here:

```txt
assignments/day-08/submissions/batch-a/your-name/solution.py
```

or

```txt
assignments/day-08/submissions/batch-b/your-name/solution.py
```
