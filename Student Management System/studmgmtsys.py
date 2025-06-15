from student_class import Students


class StudentManagementSystem:
  def __init__(self, students):
    self.students = students
  
  def id_auto_generator(self):
    max_id = 0
    for stud in self.students:
      current_id = int(stud.id)
      if current_id > max_id:
        max_id = current_id
    new_id = max_id + 1
    return f"{new_id:03d}"
    

  def main_menu(self):
    print("======================")
    print("1. Enroll a new student")
    print("2. View all the students")
    print("3. Update info")
    print("4. Remove a student")
    print("5. Exit")
    print("======================")

  def enroll_student(self, student_info):
    self.students.append(student_info)
    return True

  def view_student(self):
      print("======================")
      print("Students' list:")
      print("======================\n")
      for stud in self.students:
        print(f"ID: {stud.id} Name: {stud.name}\t Age: {stud.age}\t Major: {stud.major}")

  def update_info(self, student_id, student_name, student_age, major):
    for stud in self.students:
      if stud.id == student_id:
        if student_name:
          stud.name = student_name
        if student_age:
          stud.age = student_age
        if major:
          stud.major = major
        return True
    return False
      
  def remove_student(self, student_id):
    for stud in self.students:
      if stud.id == student_id:
        self.students.remove(stud)
        return True
    return False
