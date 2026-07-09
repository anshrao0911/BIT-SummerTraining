import matplotlib.pyplot as plt
# Use this data:

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_sales = [12000, 15000, 13500, 18000, 21000, 19500]
courses = ["Python", "Data Analytics", "AI", "Machine Learning"]
students = [35, 28, 22, 18]

## Questions

### Question 1: Line Chart

# Create a line chart of `months` and `monthly_sales`.

"""- Title: `Monthly Sales`
- X-axis label: `Month`
- Y-axis label: `Sales`
- Save as `monthly_sales_line.png`"""
plt.plot(months,monthly_sales,marker="o",linewidth=3)
plt.xlabel("Month",fontsize=12)
plt.ylabel("Sales",fontsize=12)
plt.title("Monthly Sales", fontsize=16,style="italic")
plt.savefig("monthly_sales_line.png")
plt.grid()
plt.show()

### Question 2: Bar Chart

"""Create a bar chart of `courses` and `students`.

- Title: `Students by Course`
- X-axis label: `Course`
- Y-axis label: `Students`
- Save as `students_by_course_bar.png`"""
plt.bar(courses,students)
plt.xlabel("Course")
plt.ylabel("Students")
plt.title("Students by Course")
plt.savefig("students_by_course_bar.png")
plt.show()

### Question 3: Pie Chart

"""Create a pie chart of `courses` and `students`.

- Title: `Course Enrollment Share`
- Display percentage labels using `autopct`
- Save as `course_enrollment_pie.png`"""
plt.pie(students,labels=courses,autopct="%1.1f%%")
plt.title("Course Enrollment Share")
plt.savefig("course_enrollment_pie.png")
plt.show()

### Question 4: Scatter Plot

#Use these values to create a scatter plot:

study_hours = [1, 2, 3, 4, 5, 6]
marks = [45, 55, 62, 70, 82, 90]

"""- Title: `Study Hours and Marks`
- X-axis label: `Study Hours`
- Y-axis label: `Marks`
- Save as `study_hours_scatter.png`"""
plt.scatter(study_hours,marks)
plt.title("Study Hours and Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.savefig("study_hours_scatter.png")
plt.grid()
plt.show()

### Question 5: Add Grid and Legend

# Create a line chart for the monthly sales data. Add a grid and a legend named `Sales`.
plt.plot(months,monthly_sales,label="Sales")
plt.xlabel("Month",fontsize=12)
plt.ylabel("Sales",fontsize=12)
plt.title("Monthly Sales", fontsize=16,style="italic")
plt.savefig("monthly_sales_line.png")
plt.grid()
plt.legend()
plt.show()

### Question 6: Compare Two Lines

# Use these values:

python_students = [20, 25, 30, 28, 35, 40]
ai_students = [10, 12, 15, 18, 20, 22]

# Plot both lines against `months`, add a legend, title, and axis labels. Save as `course_growth.png`.
plt.plot(months, python_students, marker="o", label="Python Students")
plt.plot(months, ai_students, marker="o", label="AI Students")
plt.title("Course Growth")
plt.xlabel("Month")
plt.ylabel("Number of Students")
plt.legend()
plt.grid(True)
plt.savefig("course_growth.png")
plt.show()


### Question 7: Chart Readability

# For the bar chart from Question 2, rotate the course labels by 20 degrees and use `plt.tight_layout()` before saving.
plt.bar(courses, students)
plt.title("Students by Course")
plt.xlabel("Course")
plt.ylabel("Students")
plt.xticks(rotation=20)   # Rotate labels by 20 degrees
plt.tight_layout()        # Adjust spacing before saving
plt.savefig("students_by_course_bar_readable.png")
plt.show()

### Question 8: Reflection Comment

# Add a Python comment at the bottom of `solution.py` that explains which chart is best for comparing courses and why.
# Bar chart is best for comparing courses because whwn we have to compare between different category it shows the difference clearly.