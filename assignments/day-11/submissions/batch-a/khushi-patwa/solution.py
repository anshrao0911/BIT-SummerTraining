## Topic: Statistical Visualization With Seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# (Ques 1) Set Theme
sns.set_theme(style="whitegrid")
output_dir = Path(__file__).parent
# Student Data
student_data = {
    "name": ["Aman", "Priya", "Shalu", "Raj", "Ansh", "Neha", "Vivek", "Riya"],
    "course": ["Python", "Python", "Data Analytics", "Data Analytics", "AI", "AI", "Python", "Data Analytics"],
    "study_hours": [2, 4, 3, 5, 6, 4, 3, 5],
    "marks": [55, 78, 68, 88, 92, 82, 70, 90],
    "attendance": [72, 85, 80, 92, 95, 88, 78, 90]
}
df = pd.DataFrame(student_data)

print("="*40)

# (Ques 2) Count Plot
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="course")
plt.title("Students by Course")
plt.tight_layout()
plt.savefig(output_dir / "course_count.png")
plt.close()

print("="*40)

# (Ques 3) Bar Plot
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x="course", y="marks")
plt.title("Average Marks by Course")
plt.tight_layout()
plt.savefig(output_dir / "average_marks_bar.png")
plt.close()

print("="*40)

# (Ques 4) Scatter Plot
plt.figure(figsize=(6, 4))
sns.scatterplot(
    data=df,
    x="study_hours",
    y="marks",
    hue="course"
)
plt.title("Study Hours vs Marks")
plt.tight_layout()
plt.savefig(output_dir / "study_hours_marks_scatter.png")
plt.close()

print("="*40)

# (Ques 5) Box Plot
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="course", y="marks")
plt.title("Marks Distribution by Course")
plt.tight_layout()
plt.savefig(output_dir / "marks_boxplot.png")
plt.close()

print("="*40)

# (Ques 6) Histogram + KDE
plt.figure(figsize=(6, 4))
sns.histplot(df["marks"], kde=True)
plt.title("Marks Distribution")
plt.tight_layout()
plt.savefig(output_dir / "marks_histogram.png")
plt.close()

print("="*40)

# (Ques 7) Correlation Heatmap
plt.figure(figsize=(6, 4))
corr_matrix = df[["study_hours", "marks", "attendance"]].corr()
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="Blues"
)
plt.title("Student Metrics Correlation")
plt.tight_layout()
plt.savefig(output_dir / "student_correlation_heatmap.png")
plt.close()

print("="*40)

# (Ques 8) Best Performing Course
best_course = (
    df.groupby("course")["marks"]
      .mean()
      .idxmax()
)
print(f"Best performing course: {best_course}")