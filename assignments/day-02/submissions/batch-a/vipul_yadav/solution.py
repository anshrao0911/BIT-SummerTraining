# 1. Write a program to check whether a number is positive, negative, or zero.
print("#"*45)
print("Welcome To check the number nature.\n")

number = int(input(f"Enter the Number : "))

if number > 0:
    print("The given number is positive.")
elif number < 0:
    print ("The number is negative .")
else :
    print(" The given number is zero .") 

print("#"*45)


# 2. Write a program to check whether a number is even or odd.

print("Welcome to check number is even or odd .")
number = int(input(f"Enter the Number : "))

if number % 2 == 0:
    print("Number is even .")
else: 
    print("Number is odd .")
print("#"*45)


# 3. Create a list of 10 numbers and print each number using a loop.
number = [1,2,3,4,5,6,7,8,9,0]

for num in number:
    print(num)

print("#"*45)


# 4. Write a function named `calculate_average` that takes 3 marks and returns the average.

def calculate_average(num1 ,num2, num3):
    total_marks = num1 + num2 + num3
    average = total_marks/ 3
    return average

num1 = float(input("Enter the marks 1:"))
num2 = float(input("Enter the marks 2:"))
num3 = float(input("Enter the marks 3:"))
average = calculate_average(num1,num2,num3)
print("Average marks:", average)
print("#"*45)


# 5. Write a function named `grade_student` that prints a grade based on marks.

def grade_student(marks):
     if marks >= 90:
         print("Grade : A+")
     elif marks >= 80:
         print("Grade : A")
     elif marks >= 70:
         print("Grade : B")
     elif marks >= 60:
         print("Grade : C")
     elif marks >= 50:
         print("Grade : D")
     else:
         print("Grade : E")

marks1 = float(input("Enter the marks of Physics:"))
marks2 = float(input("Enter the marks of Chemistry:")) 
marks3 = float(input("Enter the marks of Maths:"))  
marks4 = float(input("Enter the marks of Hindi:"))
marks5 = float(input("Enter the marks of English:"))          
marks6 = float(input("Enter the marks of Computer:"))   
total_marks = marks1 + marks2 + marks3 + marks4 + marks5 + marks6    
average_marks = total_marks/6
grade_student(average_marks)            
print("#"*45)