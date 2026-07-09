# Creating a list and printing it
student_name=["nandini","priya","radha","shalu","priyanshi"]
for item in student_name:
    print(item)
 # Adding a new name to  list 
student_name.append("rose")    
print(student_name)
 # Creating a tuple o five cities
cities=("gorakhpur","lucknow","varanasi","deoria","ayodhya")
print(cities[1])
# Creatin a set of 5 courses
courses={"B.tech","MBA","BCA","LLB","M.tech"}
for item in courses:
    print(item)
# Adding a new course to set
courses.add("Diploma") 
print(courses)   
# Creating a dictionary for one student
student_rec={"Name":"Priya",
             "Branch":"AIML",
             "Batch":"A Batch",
             "Marks":9}
# Printing in readable formate
for item in student_rec:
    print(item,"   ",student_rec[item])
