# ==========================================
#            BASIC QUESTIONS
# ==========================================

# Question 1: List Append
students = ['Aman', 'Priya', 'Shalu', 'Raj', 'Ansh']
students.append('Vivek')
print(students)
# Expected Output: ['Aman', 'Priya', 'Shalu', 'Raj', 'Ansh', 'Vivek']


# Question 2: Tuple Indexing
cities = ('Gorakhpur', 'Lucknow', 'Delhi', 'Mumbai', 'Patna')
print(cities[2]) # Index 2 matlab 3rd item
# Expected Output: Delhi


# Question 3: Set Add
courses = {'Python', 'Data Analytics', 'Machine Learning', 'SQL'}
courses.add("AI")
print(sorted(list(courses))) # Sort karke list mein print kiya
# Expected Output: ['AI', 'Data Analytics', 'Machine Learning', 'Python', 'SQL']


# Question 4: Dictionary Access
student = {
    'name': 'Rahul',
    'course': 'Python Data AI',
    'batch': 'Batch-B',
    'city': 'Delhi'
}
print(f"Name: {student['name']}")
print(f"Course: {student['course']}")
# Expected Output:
# Name: Rahul
# Course: Python Data AI


# ==========================================
#           MEDIUM QUESTIONS
# ==========================================

# Question 5: Filter Even Numbers
numbers = list(range(1, 11)) # 1 se 10 tak ki list
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
# Expected Output: [2, 4, 6, 8, 10]


# Question 6: Count Word Frequency
words = ["python", "ai", "python", "data", "ai", "python"]
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)
# Expected Output: {'python': 3, 'ai': 2, 'data': 1}


# Question 7: Nested Student Dictionary
student_data = {
    'name': 'Neha',
    'marks': {'python': 85, 'data': 90},
    'skills': ['Python', 'SQL']
}
student_data['skills'].append('Pandas')
print(student_data)
# Expected Output: {'name': 'Neha', 'marks': {'python': 85, 'data': 90}, 'skills': ['Python', 'SQL', 'Pandas']}


# Question 8: Common Elements
python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}

common_students = python_students.intersection(ai_students)
print(sorted(list(common_students)))
# Expected Output: ['Neha', 'Raj']