# 1. Create a list of 5 student names and print all names
students = ["Avinash", "Anna", "Alok", "Rahul", "Priya"]

print("Student Names:")
for student in students:
    print(student)

# 2. Add one new student name to the list
students.append("Rohit")

print("\nUpdated Student List:")
print(students)

# 3. Create a tuple of 5 city names and print the second city
cities = ("Gorakhpur", "Lucknow", "Delhi", "Mumbai", "Kanpur")

print("\nSecond City:")
print(cities[1])

# 4. Create a set of 5 course names and add one new course
courses = {"Python", "Java", "C++", "HTML", "CSS"}
courses.add("Data Science")

print("\nCourses:")
print(courses)

# 5. Create a dictionary for one student
student_info = {
    "name": "Avinash Yadav",
    "branch": "CS",
    "batch": "2025-26",
    "marks": 85
}

# 6. Print the student dictionary in a readable format
print("\nStudent Information:")
print("Name :", student_info["name"])
print("Branch :", student_info["branch"])
print("Batch :", student_info["batch"])
print("Marks :", student_info["marks"])