# Q.1. Create a list of 5 student names and print all names.
students = ["Naruto","Hinata","Sakura","Sasuke","Shikamaru"]
print(students)

# Q.2. Add one new student name to the list.
students = ["Naruto","Hinata","Sakura","Sasuke","Shikamaru"]
students.append("Ino")
print(students)

# Q.3. Create a tuple of 5 city names and print the second city.
city = ("Gorakhpur","Delhi","Mumbai","Lucknow","Darjeling")
print(city[1])

# Q.4. Create a set of 5 course names and add one new course.
course = {"B.Sc","B.Tech","B.Pharma","B.C.A","B.A"}
course.add("Management")
print(course)

# Q.5. Create a dictionary for one student with name, branch, batch, and marks.
student = {
    "name":"Ansh",
    "branch":"Data Science",
    "batch":"2024-2028",
    "marks":"83"
}
print("Name:",student["name"])
print("Branch:",student["branch"])
print("Batch:",student["batch"])
print("Marks:",student["marks"])

# Q.6. Print the student dictionary in a readable format.
student = {
    "name":"Ansh",
    "branch":"Data Science",
    "batch":"2024-2028",
    "marks":"83"
}
for key,value in student.items():
    print(f"{key.capitalize()}:{value}")

