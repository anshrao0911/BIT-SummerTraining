#1. Create a list of 5 student names and print all names.
#list of students
student_names = ["raj","aryan","rajnish","priya","mangal"]
print(student_names)   #printing the list of students.

print("_"*45)      #line for separation of different questions.


# 2. Add one new student name to the list.

student_names = ["raj","aryan","rajnish","priya","mangal"]
student_names.append("ayush")            #adding new student name in end of the list
print(student_names)                     #print the new list of students.


print("_"*45)

#3. Create a tuple of 5 city names and print the second city.

cities_names = ("gorakhpur","lucknow","kanpur","varanasi","agra")
print(cities_names[1])           #printing the second city name with index first

print("_"*45)
#4. Create a set of 5 course names and add one new course.

course_names = {"python","java","c++","c","javascript"}
course_names.add("html")
print(course_names)

print("_"*45)

#5. Create a dictionary for one student with name, branch, batch, and marks.

student_dict = {
    "name": "raj singh",
    "branch": "computer science",
    "batch": 2024,
    "marks": [85,90,78,92],
}



#6. Print the student dictionary in a readable format.

for key, value in student_dict.items():  #iterating the dictionary of using key and value
    print(f"{key}: {value}")             #printing the key and value in a readable format.

print("_"*45)                            # line for separation of different questions.