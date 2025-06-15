from student_class import Students

#load
def load_data(filename):
    students = []
    with open (filename, "r") as file:
        for line in file:
            student_id, student_name, student_age, major = line.strip().split(",")
            loaded_students = Students(student_id, student_name, student_age, major)
            students.append(loaded_students)
    return students

#save
def save_data(students, filename):
    with open (filename, "w") as file:
        for stud in students:
            file.write(f"{stud.stud_id}, {stud.stud_name}, {stud.stud_age}, {stud.major}\n")