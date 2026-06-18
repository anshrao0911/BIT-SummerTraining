# 1. Add student
# 2. View all students
# 3. Search student
# 4. Update marks
# 5. Delete student
# 6. Show average marks
# 7. Show topper
# 8. Exit

FILE_NAME = "students.txt"


def add_student():
    name = input("Enter Student Name: ")
    marks = input("Enter marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(name + "," + marks + "\n")
    print("Student Added Successfully!")

def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if len(data) == 0:
                print("No Records FOund")
                return
            print("\n -- Student Records --")

            for line in data:
                name, marks = line.strip().split(",")
                print("Name:", name, "| Marks:", marks)
    except FileNotFoundError:
        print("No File Found. Please add students first")

def search_students():
    search_name = input("Enter Student name to search: ")
    found = False
    try: 
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, marks = line.strip() .split(",")
                if name.lower() == search_name.lower():
                    print("Student Found!")
                    print("Name:", name)
                    print("Marks:", marks)
                    found = True
                    break
        if not found:
            print("Student not found")
    except FileNotFoundError:
        print("No File Foudn. Please add students first")

def update_marks():
    search_name = input("Enter student name to update: ")
    new_marks = input("Enter new marks: ")

    updated_lines = []
    found = False
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, marks = line.strip().split(",")

                if name.lower() == search_name.lower():
                    updated_lines.append(name + ","
                         + new_marks + "\n")
                    found = True
                else:
                    updated_lines.append(line)
        with open(FILE_NAME, "w") as file:
            file.writelines(updated_lines)
        if found:
            print("Marks Updated Successfully.")
        else:
            print("Student not found")
    except FileNotFoundError:
        print("No File Found. Please add students first")

def delete_student():
    delete_name = input("Enter student name: ")

    new_lines = []
    found = False

    try: 
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, marks = line.strip().split(",")
                if name.lower() == delete_name.lower():
                    found = True
                else:
                    new_lines.append(line)
        with open(FILE_NAME, "w") as file:
            file.writelines(new_lines)
        if found:
            print("Student deleted successfully")
        else:
            print("Studnet not found")
    except FileNotFoundError:
        print("No File Found Please add students first")

def average_marks():
    total = 0
    count = 0

    try:
        with open(FILE_NAME,"r") as file:
            for line in file:
                name, marks = line.strip().split(",")
                total += int(marks)
                count += 1
            if count == 0:
                print("No Records Found.")
            else:
                average = total /count
                print("Average Marks:", average)
    except FileNotFoundError:
        print("No File Found. Please add students first.")

def show_topper():
    topper_name = ""
    highest_mark = -1

    try: 
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, marks = line.strip().split(",")
                marks = int(marks)
                if marks > highest_mark:
                    highest_mark = marks
                    topper_name = name
        if highest_mark == -1:
            print("No Records Found.")
        else:
            print("Topper:", topper_name, "| Marks:", highest_mark)
    except FileNotFoundError:
        print("No File FOund. P;ease add students first")


while True:
    print("Student Marks Management System")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Average Marks")
    print("7. Show Topper Student")
    print("8. Exit")

    choice = input("Enter Your Choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_students()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        average_marks()
    elif choice == "7":
        show_topper()
    elif choice == "8":
        print("Thank You")
        break
    else:
        print("Invalid Choice. Please try again")
