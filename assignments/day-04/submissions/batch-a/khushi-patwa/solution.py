#  Python Data Structures


# Question 1: List Append
students = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]
students.append("Vivek")
print(students)

# Question 2: Tuple Indexing
cities = ("Mumbai", "Lucknow", "Delhi", "Patna", "Jaipur")
print(cities[2])

# Question 3: Set Add
courses = {"Python", "SQL", "Machine Learning", "Data Analytics"}
courses.add("AI")
print(sorted(courses))

# Question 4: Dictionary Access
student = {
    "name": "Rahul",
    "course": "Python Data AI",
    "batch": "A",
    "city": "Kanpur"
}

print("Name:", student["name"])
print("Course:", student["course"])

# Question 5: Filter Even Numbers
numbers = list(range(1, 11))
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

# Question 6: Count Word Frequency
words = ["python", "ai", "python", "data", "ai", "python"]

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)

# Question 7: Nested Student Dictionary
student_info = {
    "name": "Neha",
    "marks": {
        "python": 85,
        "data": 90
    },
    "skills": ["Python", "SQL"]
}

student_info["skills"].append("Pandas")
print(student_info)

# Question 8: Common Elements
python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
common_students = []
for student in python_students:
    if student in ai_students:
        common_students.append(student)

common_students.sort()

print(common_students)