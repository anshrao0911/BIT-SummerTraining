# 1. Create a list of 5 student names and print all names.
students = ["priya","monika","soni","kajal","palak"]
print(students)


# 2. Add one new student name to the list.
students.append("sonakshi")
print(students)


# 3. Create a tuple of 5 city names and print the second city.
cities = ("gujarat","mumbai","gorakhapur","maharajganj","partawal")
print(cities[1])



# 4. Create a set of 5 course names and add one new course.
course = {"java","c++","c","python","java script"}
course.add("HTML")
print(course)


# 5. Create a dictionary for one student with name, branch, batch, and marks.
student = {
    "name":"monika pandey",
    "branch":"electronics and communication engineering",
    "batch":"A",
    "marks":99

}


# 6. Print the student dictionary in a readable format.
for key,value in student.items():
    print(key,":",value)
