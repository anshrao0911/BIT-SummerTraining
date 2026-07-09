import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Use this data to create a DataFrame:

student_data = {
    "name": ["Aman", "Priya", "Shalu", "Raj", "Ansh", "Neha", "Vivek", "Riya"],
    "course": ["Python", "Python", "Data Analytics", "Data Analytics", "AI", "AI", "Python", "Data Analytics"],
    "study_hours": [2, 4, 3, 5, 6, 4, 3, 5],
    "marks": [55, 78, 68, 88, 92, 82, 70, 90],
    "attendance": [72, 85, 80, 92, 95, 88, 78, 90]
}
### Question 1: Set a Theme

# Set a Seaborn theme using `sns.set_theme(style="whitegrid")` before creating charts.
df=pd.DataFrame(student_data)
sns.set_theme(style="whitegrid")

### Question 2: Count Plot

# Create a count plot showing the number of students in each course.

#- Title: `Students by Course`
#- Save as `course_count.png`
sns.countplot(data=df, x="course")
plt.title("Students by Course")
plt.savefig("course_count.png")
plt.show()
plt.close()

### Question 3: Bar Plot

"""Create a bar plot showing the average marks for each course.

- Title: `Average Marks by Course`
- Save as `average_marks_bar.png`"""
sns.barplot(data=df, x="course", y="marks")
plt.title("Average Marks by Course")
plt.savefig("average_marks_bar.png")
plt.show()
plt.close()

### Question 4: Scatter Plot

"""Create a scatter plot showing `study_hours` on the x-axis and `marks` on the y-axis. Use `course` as the color grouping.

- Title: `Study Hours vs Marks`
- Save as `study_hours_marks_scatter.png`"""
sns.scatterplot(data=df,x="study_hours",y="marks",hue="course")
plt.title("Study Hours vs Marks")
plt.savefig("study_hours_marks_scatter.png")
plt.show()
plt.close()

### Question 5: Box Plot

"""Create a box plot of marks grouped by course.

- Title: `Marks Distribution by Course`
- Save as `marks_boxplot.png`"""
sns.boxplot(data=df,x="course",y="marks")
plt.title("Marks Distribution by Course")
plt.savefig("marks_boxplot.png")
plt.show()
plt.close()

### Question 6: Histogram

"""Create a histogram of marks with a KDE curve.

- Title: `Marks Distribution`
- Save as `marks_histogram.png`"""
sns.histplot(data=df,x="marks",kde=True)
plt.title("Marks Distribution")
plt.savefig("marks_histogram.png")
plt.show()
plt.close()

### Question 7: Correlation Heatmap

"""Create a correlation heatmap for `study_hours`, `marks`, and `attendance`.

- Use `annot=True`
- Title: `Student Metrics Correlation`
- Save as `student_correlation_heatmap.png`"""

correlation = df[["study_hours", "marks", "attendance"]].corr()
sns.heatmap(correlation, annot=True)
plt.title("Student Metrics Correlation")
plt.savefig("student_correlation_heatmap.png")
plt.show()
plt.close()

### Question 8: Best Performing Course

# Use Pandas `groupby` to find the course with the highest average marks and print it.

# Expected Output:
# Best performing course: AI
average_marks = df.groupby("course")["marks"].mean()
best_course = average_marks.idxmax()
print("Best performing course:", best_course)
