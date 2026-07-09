# Day 10 Assignment

## Topic: Data Visualization With Matplotlib

Complete all questions in one file named `solution.py`.

Use Matplotlib for this assignment. Save each chart as a PNG file in your own submission folder.

Install Matplotlib if required:

```bash
python3 -m pip install matplotlib
```

Start your program with:

```python
import matplotlib.pyplot as plt
```

Use this data:

```python
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_sales = [12000, 15000, 13500, 18000, 21000, 19500]
courses = ["Python", "Data Analytics", "AI", "Machine Learning"]
students = [35, 28, 22, 18]
```

## Questions

### Question 1: Line Chart

Create a line chart of `months` and `monthly_sales`.

- Title: `Monthly Sales`
- X-axis label: `Month`
- Y-axis label: `Sales`
- Save as `monthly_sales_line.png`

### Question 2: Bar Chart

Create a bar chart of `courses` and `students`.

- Title: `Students by Course`
- X-axis label: `Course`
- Y-axis label: `Students`
- Save as `students_by_course_bar.png`

### Question 3: Pie Chart

Create a pie chart of `courses` and `students`.

- Title: `Course Enrollment Share`
- Display percentage labels using `autopct`
- Save as `course_enrollment_pie.png`

### Question 4: Scatter Plot

Use these values to create a scatter plot:

```python
study_hours = [1, 2, 3, 4, 5, 6]
marks = [45, 55, 62, 70, 82, 90]
```

- Title: `Study Hours and Marks`
- X-axis label: `Study Hours`
- Y-axis label: `Marks`
- Save as `study_hours_scatter.png`

### Question 5: Add Grid and Legend

Create a line chart for the monthly sales data. Add a grid and a legend named `Sales`.

### Question 6: Compare Two Lines

Use these values:

```python
python_students = [20, 25, 30, 28, 35, 40]
ai_students = [10, 12, 15, 18, 20, 22]
```

Plot both lines against `months`, add a legend, title, and axis labels. Save as `course_growth.png`.

### Question 7: Chart Readability

For the bar chart from Question 2, rotate the course labels by 20 degrees and use `plt.tight_layout()` before saving.

### Question 8: Reflection Comment

Add a Python comment at the bottom of `solution.py` that explains which chart is best for comparing courses and why.

## Submission

Submit your Python file and the five required chart images:

```txt
assignments/day-10/submissions/batch-a/your-name/solution.py
assignments/day-10/submissions/batch-a/your-name/monthly_sales_line.png
assignments/day-10/submissions/batch-a/your-name/students_by_course_bar.png
assignments/day-10/submissions/batch-a/your-name/course_enrollment_pie.png
assignments/day-10/submissions/batch-a/your-name/study_hours_scatter.png
assignments/day-10/submissions/batch-a/your-name/course_growth.png
```

Use the same structure with `batch-b` when applicable.
