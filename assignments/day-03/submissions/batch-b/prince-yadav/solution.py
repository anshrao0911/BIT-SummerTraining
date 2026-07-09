# 1. Create a list of 5 student names and print all names.
students = ["Aman", "Deepak", "Prince", "Ansh", "Aradhana"]
print("All students:", students)

# 2. Add one new student name to the list.
students.append("Raj")
print("Updated student list:", students)

# 3. Create a tuple of 5 city names and print the second city.
cities = ("Gorakhpur", "Lucknow", "Delhi", "Mumbai", "Patna")
print("Second city:", cities[1]) # Index 1 matlab second item

# 4. Create a set of 5 course names and add one new course.
courses = {"Python", "Data Science", "Machine Learning", "Web Dev", "Cyber Security"}
courses.add("Cloud Computing")
print("Updated courses set:", courses)

# 5. Create a dictionary for one student with name, branch, batch, and marks.
student_info = {
    "name": "Prince Yadav",
    "branch": "Computer Science",
    "batch": "Batch-B",
    "marks": 95
}

# 6. Print the student dictionary in a readable format.
print("\n--- Student Details ---")
for key, value in student_info.items():
    print(f"{key.capitalize()}: {value}")