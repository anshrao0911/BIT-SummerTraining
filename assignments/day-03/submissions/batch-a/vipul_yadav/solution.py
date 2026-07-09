#1. Create a list of 5 student names and print all names.

print("+"*45)
students = ["Aman","Rahul","Vivek","Vikas","Aditya"]
print("Students Names :-")
for student in students:
    print (student)

print("+"*45)



# 2. Add one new student name to the list.

new_student = input("Enter new student name: ")
students.append(new_student)
print("Student add successfully!")
for student in students:
    print(student)

print("+"*45)



# 3. Create a tuple of 5 city names and print the second city.

cities = ("Delhi","Lucknow","Mumbai","Kolkata","Chennai")
print(cities[1])
print("+"*45)



# 4. Create a set of 5 course names and add one new course.

courses = {"Python","java","C","DSA","DBMS"}
print(courses)
courses.add("AI")
print("New course added successfully!")
print(courses)
print("+"*45)



# 5. Create a dictionary for one student with name, branch, batch, and marks.
student = {
    "name":"Vipul Yadav",
    "branch":"CSE",
    "batch":"A",
    "marks" : 85
    }

# 6. Print the student dictionary in a readable format.

for key ,value in student.items():
    print(key," : ",value)