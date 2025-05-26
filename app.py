# Functions
# database configuration
students = [
    {
    'id' : 1,
    'name': 'John',
    'age': 20,
    'major' : 'Computer Science'
    },
    {
    'id' : 2,
    'name': 'Alice',
    'age': 22,
    'major' : 'Mathematics'
    },

]


def search_item(id, items):
    for item in items:
        if item['id'] == id:
            return item
    else:
        return None


def create_student():
    id = input("Enter ID of a student : ")
    name = input("\nEnter the student name : ")
    age = int(input("Enter the student age: "))
    major = input("Enter the student major: ")
    new_student = {
        'id' : id,
        'name' : name,
        'age' : age,
        'major' : major
    }
    students.append(new_student)
    print(f" >>>> {new_student} is added successfully!")

def list_student():
    print("\nStudent Lists")
    print(f"==================")
    for student in students:
        print(f"{student['id']} : {student['name']} \t\t {student['age']} \t\t {student['major']}")

def update_student():
    student_id = int(input("Enter the id of the student that you wanna update info: "))
    wanted_student = search_item(student_id, students)
    if wanted_student:
        print(f"Current Info: {wanted_student}")
        name = input("Enter new name (leave blank to keep current): ")
        age = input("Enter new age (leave blank to keep current): ")
        major = input("Enter new major (leave blank to keep current): ")

        if name:
            wanted_student['name'] = name

        if age:
            wanted_student['age'] = int(age)

        if major:
            wanted_student['major'] = major

        print(f" >>>> {wanted_student} is updated successfully!")

def remove_student():
    student_id = input("Enter the student id that you wanna remove : ")
    wanted_student = search_item(student_id, students)
    students.remove(wanted_student)
    print(f"Student is removed successfully!")

def menu():
    print(f"===========================================")
    print(f"Welcome to our student enrollment system!!!")
    print(f"===========================================")

    print("1. Create a new student")
    print("2. List All Students")
    print("3. Update Student Information")
    print("4. Delete a student")
    print("5. Exit ")


def main():
    menu()
    while True:
        opt = int(input("Enter an option that you wanna do :: "))

        if opt == 1:
            create_student()
        elif opt == 2:
            list_student()
        elif opt == 3:
            update_student()
        elif opt == 4:
            remove_student()
        elif opt == 5:
            print("Good bye!!!")
            break
        else:
            print("Invalid Option : Please choose a valid one.")

main()