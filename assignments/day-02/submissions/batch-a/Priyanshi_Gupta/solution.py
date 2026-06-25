#This program checks whether a number entered by the user is positive, negative, or zero. 
num = int(input("Enter the number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")


#This program checks whether a number entered by the user is even or odd.
num = int(input("Enter the number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd") 

#This program prints the numbers from 1 to 10 using a for loop.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for list in list:
    print(list)




def calcute_average(mark1 , mark2, mark3):
    average = (mark1 + mark2 + mark3)/3
    return average

avg = calcute_average(90, 80, 70)
print("The average of the marks is:", avg)

#Function to print grade based on marks.

def grade_student(marks):
    if marks >=90:
        return "A"
    if marks >=80:
        return "B"
    if marks >=70:
        return "C"
    if marks >=60:
        return "D"  
    return "F"
grade = grade_student(85)
print("The grade of the student is:", grade)  
