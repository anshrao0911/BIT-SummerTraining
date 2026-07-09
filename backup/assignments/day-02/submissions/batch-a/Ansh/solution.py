# Q.1. Write a program to check whether a number is positive, negative, or zero.
number=int(input("Enter the number"))
if number>0:
    print("Number is positive")               #checking postive number
elif number<0:
    print("Number is negative")               #checking negative number
else:
    print("Number is zero")                   #checking zero

# Q.2. Write a program to check whether a number is even or odd.
Number=int(input("Enter the number"))
if Number%2==0:                               #checking even numbers
    print("Number is Even")
else:                                         #checking odd numbers
    print("Number is Odd")

# Q.3. Create a list of 10 numbers and print each number using a loop.
list=[1,2,3,4,5,6,7,8,9,0]
for i in list:
    print("list numbers :",i)                 #printing each numbers in list

# Q.4. Write a function named `calculate_average` that takes 3 marks and returns the average.
def calculate_average(m1,m2,m3):
    average=(m1+m2+m3)/5
    return average

m1 = float(input("Enter the marks of m1"))
m2 = float(input("Enter the marks of m2"))
m3 = float(input("Enter the marks of m3"))

result=calculate_average(m1,m2,m3)
print("Average : ",result)                    #using def function to calculate average


# Q.5. Write a function named `grade_student` that prints a grade based on marks.
def grade_student(marks):
    if marks>=90:
        grade ="A+"
    elif marks>=80:
        grade ="A"
    elif marks>=70:
        grade ="B"
    elif marks>=60:
        grade ="C"
    elif marks>=50:
        grade ="D"
    else:
        grade ="F"

    return grade
marks=float(input("Enter the marks ===>"))   
result=grade_student(marks)
print("Grade ==>",result)                   #using def function to print grade 
