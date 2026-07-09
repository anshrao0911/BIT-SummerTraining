# (Q1) Create a list of 5 student names and print all names.

# Creating a list containing five student names
student_names = ["Aarav", "Diya", "Rohan", "Sneha", "Kunal"]

# Displaying all student names one by one
print("List of Students:")
for name in student_names:
    print(name)

# (Q2) Add one new student name to the list.

# Appending a new student name to the existing list
student_names.append("Ananya")

# Displaying the updated student list
print("\nUpdated Student List:")
print(student_names)

# (Q3) Create a tuple of 5 city names and print the second city.

# Creating an immutable tuple of five city names
city_names = ("Delhi", "Lucknow", "Mumbai", "Chennai", "Jaipur")

# Printing the second city using index 1
print("\nSecond City in Tuple:")
print(city_names[1])

# (Q4) Create a set of 5 course names and add one new course.

# Creating a set containing five course names
courses = {"Python", "Java", "C++", "SQL", "AI"}

# Adding a new course to the set
courses.add("Data Analytics")

# Printing the updated course set
print("\nAvailable Courses:")
print(courses)

# (Q5) Create a dictionary for one student with name, branch, batch, and marks.

# Creating a dictionary to store student information
student = {
    "Name": " Khushi Patwa",
    "Branch": "B.Tech CSE (AI & ML)",
    "Batch": "2024-2028",
    "Marks": 90
}

# (Q6) Print the student dictionary in a readable format.

# Printing student details in a readable format
print("\nStudent Information")
print("-------------------")
print("Name   :", student["Name"])
print("Branch :", student["Branch"])
print("Batch  :", student["Batch"])
print("Marks  :", student["Marks"])
