# QUESTION 1
num=int(input("enter a number"))
if num >0:
    print( num," is positive")
elif num<0:
    print(num,"is negative")   
else:
    print("number is zero")    
# QUESTION 2
num1 = int(input("enter a number"))  
if num1%2==0:
    print("number is even")
else:
    print("number is odd") 
# QUESTION 3       
list=[1,2,3,4,5,6,7,8,9,10] 
for i in list:
    print(i)   
# QUESTION 4 
mark1=float(input("enter mark1 marks"))
mark2=float(input("enter mark2 marks"))
mark3=float(input("enter mark3 marks"))
def calculate_average(mark1,mark2,mark3):
    return (mark1+ mark2+mark3)/3
Average=round(calculate_average(mark1,mark2,mark3),2)
print("average  of mark three subject is ",Average)
 # QUESTION 5
def grade_student(marks):
    if marks>=90:
        return "A"
    elif marks>=80:
        return "B"
    elif marks>=70:
        return "C"
    elif marks>=60:
        return "D"
    else:
        return "F"

print("Grade:", grade_student(85))
