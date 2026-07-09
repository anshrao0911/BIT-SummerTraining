# day 2 assignment --------------------------------------------
# question 1 -- check the number is even or odd---
check_num = float(input("Enter the number you want to check even or odd \n"))  
if check_num%2==0:      
    print("Number is even")
else:
    print("Nmuber is odd")
print("="*45)
# question 2-------------------------
# Check whether a number is positive negative or zero
check_num2 = float(input("Enter the number to check positive , negative or zero \n "))
if check_num2 >0:
    print("Number is positive")
elif check_num2 <0:
    print("Number is negative")
else:
    print("Number is zero")
print("="*45)
# question 3--------------------------
# Create a list of 10 numbers and print each number using a loop
number_list = [10,20,30,40,50,60,70,80,90,100]
print("List of 10 numbers--")
for i in range (len(number_list)):
    print( number_list[i])
print("="*45)
# question 4-----------------------------
# Write a function named `calculate_average` that takes 3 marks and returns the average
def calculate_average(marks1,marks2,marks3):
    average=(marks1+marks2+marks3)/3
    return average

marks1=float(input("Enter the first marks to calculate average of three marks \n"))
marks2=float(input("Enter the second marks to calculate average of three numbers \n"))
marks3=float(input("Enter the third marks to calculate average of three number \n"))
result=calculate_average(marks1,marks2,marks3)
print("The Average marks of the three subject are : ",round(result,3))
print("="*45)
# question 5------------------------------------------
# Write a function named `grade_student` that prints a grade based on marks
def grade_student(total_marks):
    
    if total_marks >=450:
        print("Grade A")
    elif total_marks >=400:
        print("Grade B")
    elif total_marks >=300:
        print("Grade C")
    elif total_marks>=250:
        print("Grade D")
    else:
        print("Fail")

student_marks1=float(input("Enter the  marks of subject 1 to check grade \n"))
student_marks2=float(input("Enter the marks of subject 2 to check grade\n"))
student_marks3=float(input("Enter the marks of subject 3 to check grade\n"))
student_marks4=float(input("Enter the  marks of subject 4 to check grade\n"))
student_marks5=float(input("Enter the  marks of subject 5 to check grade\n"))
    
total_marks = student_marks1+student_marks2+ student_marks3+ student_marks4+student_marks5
student=grade_student(total_marks)