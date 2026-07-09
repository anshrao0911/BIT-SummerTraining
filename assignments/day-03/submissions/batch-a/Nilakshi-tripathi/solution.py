# Question 1: Create a list of 5 student names and print all names

students = ["Nilakshi", "Anjali", "Rahul", "Aman", "Priya"]

print("Student Names:")
for student in students:
    print(student)


# Question 2: Add one new student name to the list

students.append("Riya")

print("\nUpdated Student List:")
for student in students:
    print(student)


# Question 3: Create a tuple of 5 city names and print the second city

cities = ("Lucknow", "Delhi", "Mumbai", "Kolkata", "Bangalore")

print("\nSecond City:", cities[1])


# Question 4: Create a set of 5 course names and add one new course

courses = {"Python", "Java", "C++", "DBMS", "HTML"}

courses.add("JavaScript")

print("\nCourses:")
for course in courses:
    print(course)


# Question 5: Create a dictionary for one student

student_info = {
    "name": "Nilakshi Tripathi",
    "branch": "CSE",
    "batch": "Batch A",
    "marks": 88
}


# Question 6: Print the student dictionary in a readable format

print("\nStudent Information:")
print("Name:", student_info["name"])
print("Branch:", student_info["branch"])
print("Batch:", student_info["batch"])
print("Marks:", student_info["marks"])