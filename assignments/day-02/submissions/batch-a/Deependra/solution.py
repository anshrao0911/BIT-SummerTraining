# 1. check whether a number is positive or negative or zero
num = float(input("Enter a number:--> "))
if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")

# 2. check whether a number is even or odd
num = int(input("Enter a number:--> ")) 
if num % 2 == 0:        
    print(f"{num} is even.")                        
else:
    print(f"{num} is odd.")

# 3. create a list of 10 numbers and print each number using a loop
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in nums:
    print(n ,end=" ")  #end=" " is used to print numbers in the same line with space

# 4. Function to calculate average of 3 marks
def calculate_average(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3
    return average  
average_marks = calculate_average(85, 90, 95)
print(f"\nAverage marks: {average_marks}")

# 5. Function to print grade based on marks
def grade_student(marks):
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

grade_student(85)  #    
