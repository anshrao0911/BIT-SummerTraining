#  1. Print your name, age, and college name.

print(" Name = Vipul Yadav \n age = 20 \n Collage = BIT")

print("*"*45)

#2. Create variables for name, age, marks, and city.

name = "Vipul Yadav"
age = 20
marks = 85
city = "Gorakhpur"


# 3. Use these data types: string, integer, float, and boolean.

name = "Vipul Yadav"
age = 20
marks = 85.5
is_student = True

print(type(name))
print(type(age))
print(type(marks))
print(type(is_student))
print("*"*45)


# 4. Create a list of 5 numbers and print the list.

points = [2,5,4,8,9]

for point in points:
    print(point)

print("*"*45)


# 5. Create a dictionary with name, course, city, and batch.

students = {
    "name":" Vipul Yadav ",
    "city":" Gorakhpur ", 
    "course":" Data science ", 
    "Batch":"A"
    }

for keys , values in students.items():
    print(keys,":",values)

print("*"*45)

#6. Write one comment explaining what your program does.

# This Program explain the use of print(), variables, datatype, list and dictionary
