# 1. Create a list of 5 student names and print all names.
stu_list = ["Arsha", "Ajushi", "Park", "Yoongi", "Preet"]
print("Here each student name: ")
for name in stu_list:
    print(name)

# 2. Add one new student name to the list.
stu_list.append("Shruti")
print(stu_list)

# 3. Create a tuple of 5 city names and print the second city.
city = ("Gorakhpur", "Lucknow", "Hydrabad", "Mumbai","Delhi")
print(city[1])

# 4. Create a set of 5 course names and add one new course.
course_set = {"B.Tech", "BCA", "MBBS", "B.Pharma", "B.Com"}
course_set.add("MBA")
print(course_set)

# 5. Create a dictionary for one student with name, branch, batch, and marks.
stu_dic ={
    "name":"Aradhana",
    "branch":"ECE",
    "batch": "A",
    "Marks": 855
}

# 6. Print the student dictionary in a readable format.
for key,value in stu_dic.items():
    print(f"{key}:{value}")
