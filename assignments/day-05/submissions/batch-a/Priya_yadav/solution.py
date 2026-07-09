# 1. Creating a file named student.txt
with open("student.txt","w") as file:
    file.write("Name : Rahul\n")
    file.write("Age : 20\n")
    file.write("College Name : Buddha Institute of Technology")
    print("File created successfully")
# 2. Reading data from file and printing onto consol    
try:    
    with open("student.txt","r") as file:
        print(file.read())  
except FileNotFoundError:
     print("file not found")
# 3. Appending data in a existing file  and printing onto consol           
with open("student.txt","a") as file:
    file.write("\nCourse : Python Data AI") 
    file.write("\nCity : Gorakhpur")
try:    
    with open("student.txt","r") as file:
            print(file.read())
except FileNotFoundError:
       print("file not found")
# 4. Counting lines a file       
try:
    with open ("student.txt","r") as file:
        lines=file.readlines()
    print("Total Lines :",len(lines)) 
except FileNotFoundError:
     print("file not found ") 
# 5. creating a file named students.txt           
with open("students.txt","w") as file:
     file.write("Aman\n")
     file.write("Priya\n")
     file.write("Shalu\n")
     file.write("Raj\n")
     file.write("Ansh\n")
try:     
    with open("students.txt","r") as file: 
        data=file.read() 
        print(data) 
except FileNotFoundError:
    print("file not found")
# 6. Searching a name in file students.txt    
name=input("enter name to search")
try:
    with open("students.txt","r") as file:
        data=file.read()
        if name in data:
            print("Found")
            
        else:
            print("Not Found")

except FileNotFoundError:
     print("file not found")
# 7. copying content from  file students.txt to student_backup.txt 
file1=open("students.txt","r")
file2=open("students_backup.txt","w")
for lines in file1:
     file2.write(lines)
print("Backup created successfully")
file1.close()
file2.close() 
with open("marks.txt","w") as file:
     file.write("85\n")
     file.write("90\n")
     file.write("78\n")
     file.write("92\n")
     file.write("88\n")
with open("marks.txt","r") as file:
    data=file.read()
    print(data)
          
     