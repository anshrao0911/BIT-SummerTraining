# Day 3 Assignment ------------------------------
# Question 1---Create a list of 5 student names and print all names---
print("="*50)
student_name = ["shalu","saniya","priya","nandini","priyanshi"] # creating a list of student names
print(student_name) # print all the items of list
print("="*50)

# Question 2 -- Add one new student name to the list ----
student_name.append("shine") # Adding new element to the existing list
print(student_name) # print after adding new element
print("="*50)

# Question 3 -- Create a tuple of 5 city names and print the second city--
city_name = ("Gorakhpur","Ayodhya","Banaras","Devariya","Allahabad") # crfeating a tuple of city names
print(city_name[1]) # print index 1 value 2 of the tuple
print("="*50)

# Question 4-- Create a set of 5 course names and add one new course--
course_name = {"MBA","B.Tech","Diploma","BBA","LLB"} # creating a set of course names
print(course_name) # print the set
course_name.add("B.Pharma") # adding a new element to the set
print(course_name) # print the set after adding new element
print("="*50)

# Question 5--Create a dictionary for one student with name, branch, batch, and marks
student = {
    "name":"shalu",
    "branch":"AIML",
    "batch":"A",
    "marks":20
} # creating a dictonary of student detail
print(student) # print the dictonary in key value format
print("="*50)

# Question 6 --Print the student dictionary in a readable format--
for detail in student: # iterate the dictonay
    print(detail,student[detail]) # print the dictonary in readable format
print("="*50)