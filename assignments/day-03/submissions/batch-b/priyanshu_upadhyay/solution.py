# 1. Create a list of 5 student names and print all names.
student_names = ["Priyanshu", "Rohit", "Sneha", "Kavya", "Manish"]
print("List of students:", student_names)

# 2. Add one new student name to the list.

student_names.append("Vikram")
print("After adding new student:", student_names)

# 3. Create a tuple of 5 city names and print the second city.

city_tuple = ("Prayagraj", "Varanasi", "Kanpur", "Agra", "Noida")
print("The second city is:", city_tuple[1])

# 4. Create a set of 5 course names and add one new course.

course_set = {"Python", "Java", "C++", "Web Development", "DSA"}
course_set.add("Artificial Intelligence")
print("Final course set:", course_set)

# 5. Create a dictionary for one student with name, branch, batch, and marks.
student_info = {
    "name": "Priyanshu Upadhyay",
    "branch": "Computer Science",
    "batch": "B",
    "marks": 88
}

# 6. Print the student dictionary in a readable format.

print("\n--- Student Information ---")
for key, value in student_info.items():
    print(f"{key.capitalize()} -> {value}")