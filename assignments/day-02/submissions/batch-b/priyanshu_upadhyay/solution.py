# 1. Check whether a number is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is zero")

# 2. Check whether a number is even or odd.
num2 = int(input("Enter another number: "))
if num2 % 2 == 0:
    print(f"{num2} is even")
else:
    print(f"{num2} is odd")

# 3. Create a list of 10 numbers and print each using a loop.
numbers = [10, 20, 30, 40, 22, 33, 44, 55, 66, 77]
print("List of numbers:")
for n in numbers:
    print(n)

# 4. Function calculate_average that takes 3 marks and returns the average.
def calculate_average(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return average

result = calculate_average(40, 50, 80)
print(f"Average marks: {result}")

# 5. Function grade_student that prints a grade based on marks.
def grade_student(mark):
    if not (0 <= mark <= 100):
        print("Invalid mark. Please enter a value between 0 and 100")
    elif mark >= 90:
        print("Grade: A")
    elif mark >= 80:
        print("Grade: B")
    elif mark >= 70:
        print("Grade: C")
    elif mark >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

grade_student(85)