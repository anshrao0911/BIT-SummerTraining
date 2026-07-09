### Question 1: List Append
# Create a list of 5 student names. Add one new student name to the list and print the final list.
# Expected Output:
# ['Aman', 'Priya', 'Shalu', 'Raj', 'Ansh', 'Vivek']
student_name = ["Aman","Priya","Shalu","Raj","Ansh"]
student_name.append("Vivek")
print(student_name)
print("="*45)

### Question 2: Tuple Indexing

# Create a tuple of 5 city names and print the third city.
# Expected Output:
# Delhi
city_names = (" Gorakhpur","Allahabad","Delhi","Khalilabad","Dewariya")
print(city_names[2])
print("="*45)

### Question 3: Set Add

# Create a set of 4 course names. Add `"AI"` to the set and print the sorted list of courses.
# Expected Output:
# ['AI', 'Data Analytics', 'Machine Learning', 'Python', 'SQL']
course_names = {"Data Analytics","Machine Learning","Python","SQL"}
course_names.add("AI")
course_name=list(course_names)
print(sorted(course_name))
print("="*45)

### Question 4: Dictionary Access

# Create a dictionary with keys `name`, `course`, `batch`, and `city`. Print the student's name and course.
# Expected Output:
# Name: Rahul
# Course: Python Data AI
detail ={
    "name":"Rahul",
    "course":"Python Data AI",
    "batch":"A",
    "city":"GKP"
}
print("Name:",detail["name"])
print("Course:",detail["course"])
print("="*45)


### Question 5: Filter Even Numbers

# Create a list of numbers from 1 to 10. Create a new list that contains only even numbers and print it.
# Expected Output:
# [2, 4, 6, 8, 10]
lis =[1,2,3,4,5,6,7,8,9,10]
lis2=[]
for num in lis:
    if num%2==0:
        lis2.append(num)
print(lis2)
print("="*45)

### Question 6: Count Word Frequency

# Create a list of words:
# words = ["python", "ai", "python", "data", "ai", "python"]
# Use a dictionary to count how many times each word appears and print the dictionary.

# Expected Output:
# {'python': 3, 'ai': 2, 'data': 1}
words = ["python", "ai", "python", "data", "ai", "python"]
dict1 ={}
for ch in words:
    if ch in dict1:
        dict1[ch]+=1
    else:
        dict1[ch]=1

print(dict1)

## Question 7: Nested Student Dictionary
# Create a nested dictionary for one student with name, marks, and skills. Add one new skill "Pandas"
# and print the updated dictionary.

# Expected Output:
# {'name': 'Neha', 'marks': {'python': 85, 'data': 90}, 'skills': ['Python', 'SQL', 'Pandas']}

student = {
    
        "name":"Neha",
        "marks":{
            "python":85,
            "data":90,
        },
        "skills":["Python","SQL"]
    
}
student["skills"].append("Pandas")      
print(student)
print("="*45)

### Question 8: Common Elements
# Create two sets:
# Find the common students and print them as a sorted list.
# python_students = {"Aman", "Priya", "Raj", "Neha"}
# ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
# Expected Output:
# ['Neha', 'Raj']

python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
l1=[]
for i in python_students:
    if i in ai_students:
        l1.append(i)
print(sorted(l1))
print("="*45)