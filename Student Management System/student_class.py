class Students:
    def __init__(self, student_id, name, age, major):
        self.id = student_id
        self.name = name
        self.age = age
        self.major = major

    def display_info(self):
        return (f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Major: {self.major}")