# Day 11 Assignment

## Topic: Statistical Visualization With Seaborn

Complete all questions in one file named `solution.py`.

Use Pandas and Seaborn. Save each required chart as a PNG file in your own submission folder.

Install the libraries if required:

```bash
python3 -m pip install pandas seaborn matplotlib
```

Start your program with:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

Use this data to create a DataFrame:

```python
student_data = {
    "name": ["Aman", "Priya", "Shalu", "Raj", "Ansh", "Neha", "Vivek", "Riya"],
    "course": ["Python", "Python", "Data Analytics", "Data Analytics", "AI", "AI", "Python", "Data Analytics"],
    "study_hours": [2, 4, 3, 5, 6, 4, 3, 5],
    "marks": [55, 78, 68, 88, 92, 82, 70, 90],
    "attendance": [72, 85, 80, 92, 95, 88, 78, 90]
}
```

## Questions

### Question 1: Set a Theme

Set a Seaborn theme using `sns.set_theme(style="whitegrid")` before creating charts.

### Question 2: Count Plot

Create a count plot showing the number of students in each course.

- Title: `Students by Course`
- Save as `course_count.png`

### Question 3: Bar Plot

Create a bar plot showing the average marks for each course.

- Title: `Average Marks by Course`
- Save as `average_marks_bar.png`

### Question 4: Scatter Plot

Create a scatter plot showing `study_hours` on the x-axis and `marks` on the y-axis. Use `course` as the color grouping.

- Title: `Study Hours vs Marks`
- Save as `study_hours_marks_scatter.png`

### Question 5: Box Plot

Create a box plot of marks grouped by course.

- Title: `Marks Distribution by Course`
- Save as `marks_boxplot.png`

### Question 6: Histogram

Create a histogram of marks with a KDE curve.

- Title: `Marks Distribution`
- Save as `marks_histogram.png`

### Question 7: Correlation Heatmap

Create a correlation heatmap for `study_hours`, `marks`, and `attendance`.

- Use `annot=True`
- Title: `Student Metrics Correlation`
- Save as `student_correlation_heatmap.png`

### Question 8: Best Performing Course

Use Pandas `groupby` to find the course with the highest average marks and print it.

```python
# Expected Output:
# Best performing course: AI
```

## Submission

Submit your Python file and all six chart images:

```txt
assignments/day-11/submissions/batch-a/your-name/solution.py
assignments/day-11/submissions/batch-a/your-name/course_count.png
assignments/day-11/submissions/batch-a/your-name/average_marks_bar.png
assignments/day-11/submissions/batch-a/your-name/study_hours_marks_scatter.png
assignments/day-11/submissions/batch-a/your-name/marks_boxplot.png
assignments/day-11/submissions/batch-a/your-name/marks_histogram.png
assignments/day-11/submissions/batch-a/your-name/student_correlation_heatmap.png
```

Use the same structure with `batch-b` when applicable.
