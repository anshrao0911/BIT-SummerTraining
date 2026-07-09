# Question 1: Check whether a number is positive, negative, or zero

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Question 2: Check whether a number is even or odd

num = int(input("\nEnter another number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Question 3: Create a list of 10 numbers and print each number using a loop

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\nNumbers in the list:")
for number in numbers:
    print(number)


# Question 4: Function to calculate average of 3 marks

def calculate_average(mark1, mark2, mark3):
    return (mark1 + mark2 + mark3) / 3


avg = calculate_average(85, 90, 80)
print("\nAverage Marks:", avg)


# Question 5: Function to print grade based on marks

def grade_student(marks):
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    elif marks >= 40:
        print("Grade D")
    else:
        print("Grade F")


print("\nStudent Grade:")
grade_student(avg)