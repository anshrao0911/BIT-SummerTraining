#1
students = ["Moni", "Priya", "Priyanshi", "Mina", "Rajan"]
students.append("Mona")
print(students)

#2
cities = ("Mumbai", "Gkp", "Lucknow", "Delhi", "Malaysiya")
print(cities[2])

#3
courses = {"Python", "Java", "C++", "CSE", "HTML"}
courses.add("Data Analytics")
print(sorted(courses))

#4
student = {
    "name": "Mona",
    "course":"Python Data AI",
    "batch":"A",
    "city":"GKP"
    
}
print("Name:", student["name"])
print("Course:", student["course"])

#5
numbers = list(range(1, 11))
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)


#6
words = ["Python", "Java", "Java", "Python", "Data"]
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)

#7
student_info ={
    "name": "Priya",
    "marks":{
        "python": 85,
        "data": 90
    },
    "skills": ["Python", "SQL"]
}
student_info["skills"].append("Pandas")
print(student_info)

#8
python_students = {"Priya", "Priyanshi", "Nandini", "Mona"}
ai_students ={"Nonu", "Pagal", "Nanu", "Priya"}
common_students = []
for student in python_students:
    if student in ai_students:
       common_students.append(student)

common_students.sort()
print(common_students)
