
# Topic: Python File Handling

# Question 1: Create and Write a File

file = open("student.txt", "w")
file.write("Name: Khushi Patwa\n")
file.write("Age: 20\n")
file.write("College: BIT\n")
file.close()

print("File created successfully")


# Question 2: Read a File

file = open("student.txt", "r")
content = file.read()
file.close()
print("\nStudent Details:")
print(content)


# Question 3: Append to a File

file = open("student.txt", "a")
file.write("Course: Python Data AI\n")
file.write("City: Gorakhpur\n")
file.close()
file = open("student.txt", "r")

print("Updated File Content:")
print(file.read())

file.close()


# Question 4: Count Total Lines

file = open("student.txt", "r")
lines = file.readlines()
file.close()

print("Total lines:", len(lines))


# Question 5: Write Multiple Students

file = open("students.txt", "w")
file.write("Aman\n")
file.write("Priya\n")
file.write("Shalu\n")
file.write("Raj\n")
file.write("Ansh\n")
file.close()

file = open("students.txt", "r")
print("\nStudent Names:")
for name in file:
    print(name.strip())
file.close()


# Question 6: Search Student Name

search_name = input("\nEnter student name to search: ")
file = open("students.txt", "r")
names = file.read().splitlines()
file.close()
if search_name in names:
    print("Found")
else:
    print("Not Found")


# Question 7: Copy File Content

source = open("students.txt", "r")
data = source.read()
source.close()
backup = open("students_backup.txt", "w")
backup.write(data)
backup.close()

print("Backup created successfully")


# Question 8: Marks File Summary

file = open("marks.txt", "w")
file.write("85\n")
file.write("90\n")
file.write("78\n")
file.write("92\n")
file.write("88\n")
file.close()

file = open("marks.txt", "r")
marks = file.readlines()
file.close()

total = 0

for mark in marks:
    total = total + int(mark.strip())
average = total / len(marks)
print("\nMarks Summary")
print("Total marks:", total)
print("Average marks:", average)