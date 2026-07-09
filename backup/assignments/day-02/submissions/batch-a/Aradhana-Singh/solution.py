# 1. Write a program to check whether a number is positive, negative, or zero.
num = int(input("Enter the number: "))
if num>0:
    print(f"{num} is positive number.")
elif num<0:
    print(f"{num} is negative number.")
else:
    print("Given number is 0.")

# 2. Write a program to check whether a number is even or odd.
num = int(input("Enter a number: "))
if num%2 ==0:
    print(f"{num} is even number.")
else:
    print(f"{num} is odd number.")

# 3. Create a list of 10 numbers and print each number using a loop.
a_list = [12, 26 , 56 ,8 , 7 ,15 ,66 ,33, 17, 89]
print("Each element of the given list is: ")
for i in a_list:
    print(i)

# 4. Write a function named `calculate_average` that takes 3 marks and returns the average.
def calculate_average(mark1, mark2, mark3):
    avg = (mark1 + mark2 + mark3)/3
    return avg
print(calculate_average(14,56,32))

# 5. Write a function named `grade_student` that prints a grade based on marks.
def grade_student(phy, chem, math, eng, hindi, comp):
    total_marks = phy+ chem + math + eng + hindi + comp
    num_per = (total_marks/600) *100
    if num_per> 90:
        print("Grade: A+")
    elif num_per >80:
        print("Grade: A")
    elif num_per>70:
        print("Grade: B")
    elif num_per>60:
        print("Grade: C")
    elif num_per>50:
        print("Grade: D")
    else:
        print("Grade: E") 
    return num_per

phy = int(input("Enetr Physics marks: "))
chem = int(input("Enter Chemistry marks: "))
math = int(input("Enter Math marks: "))
eng = int(input("Enter English marks: "))
hindi = int(input("Enter Hindi marks: "))
comp = int(input("Enter Computer marks: "))
print(grade_student(phy, chem, math, eng, hindi, comp))