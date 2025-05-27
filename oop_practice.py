class Human():
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def walk(self):
        print(f"{self.name} is walking.")

human = Human("George", 20, "Student")



human.walk()