# Day 4 Assignment
#==========================================================>>>
### Question 1: List Append
#.Create a list of 5 student names. Add one new student name to the list and print the final list.
student_names = ["Aliya", "Shalu", "Ansh", "Aman", "Niya"]
new_student = "Saniya"
student_names.append(new_student)
print("Updated list of student names:")
print(student_names)                 # Adding a new student name to the list and printing the updated list    
print("="*50)
#==========================================================>>>
### Question 2: Tuple Indexing
#.Create a tuple of 5 city names and print the third city.
city_names = ("Gorakhpur", "Lucknow", "Delhi", "Mumbai", "Kolkata")
print(f"The third city in the tuple is: {city_names[2]}")         
print("="*50)                                                              # Creating a tuple of city names and printing the third city
#==========================================================>>>                                                  
### Question 3: Set Add
#.Create a set of 4 course names. Add `"AI"` to the set and print the sorted list of courses.
course_names = {"Data Science", "Machine Learning", "Artificial Intelligence", "Python Programming"}
course_names.add("AI")
print("Updated set of course names (sorted):")
print(sorted(course_names))                                           # Creating a set of course names, adding "AI" to the set and printing the sorted list of courses
print("="*50)
#=========================================================>>>
### Question 4: Dictionary Access
#.Create a dictionary with keys `name`, `course`, `batch`, and `city`. Print the student's name and course.
student_info = {
    "name": "Saniya Parveen",
    "course": "Data Science",
    "batch": "A",
    "city": "Gorakhpur"
}
print(f"Student Name: {student_info['name']}")
print(f"Student Course: {student_info['course']}")   # Creating a dictionary with student information and printing the name and course
print("="*50)
#=========================================================>>>
### Question 5: Filter Even Numbers
#.Create a list of numbers from 1 to 10. Create a new list that contains only even numbers and print it.
numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Even numbers from the list: {even_numbers}")                     # Creating a list of numbers from 1 to 10 and filtering even numbers
print("="*50)
#=========================================================>>>
### Question 6: Count Word Frequency
#.Create a list of words:
#Use a dictionary to count how many times each word appears and print the dictionary.
words = ["python", "ai", "python", "data", "ai", "python"]
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Word Frequency Count:")
print(word_count)                                                        # Creating a list of words and counting the frequency of each word using
print("="*50)
#=========================================================>>>
### Question 7: Nested Student Dictionary
#.Create a nested dictionary for one student with name, marks, and skills. Add one new skill `"Pandas"` and print the updated dictionary
student_info = {
    "name": "Saniya Parveen",
    "marks": {"python": 85, "data": 90},
    "skills": ["Python", "SQL"]
}
student_info["skills"].append("Pandas")
print("Updated Student Information:")
print(student_info)                                                      # Creating a nested dictionary for a student, adding a new skill and printing the updated dictionary   
print("="*50)
#=========================================================>>>
### Question 8: Common Elements
# Create two sets:
python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
#Find the common students and print them as a sorted list.
common_students = python_students.intersection(ai_students)
print("Common students in both sets (sorted):")
print(sorted(common_students))                                           # Creating two sets of students, finding common students and printing them as a sorted list
print("="*50)