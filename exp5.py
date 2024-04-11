#Satish Singh-22AD1003

class Person:
    def __init__(self,id, name, age, grade):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"ID : {self.id}\nName: {self.name}\nAge: {self.age}\nGrade: {self.grade}")

class Sports(Person):
    def __init__(self,id, name, age, grade, sports_grade):
        super().__init__(id, name, age, grade)
        self.sports_grade = sports_grade

    def get_details(self):
      super().display()
      print(f"Sports Grade: {self.sports_grade}")

obj1 = Sports('22AD1003', 'Satish', '20', '99', '90')
obj1.get_details()
print()
obj2 = Sports('22AD1009', 'Ram', '18', '90', '90')
obj2.get_details()
print()
obj2 = Sports('22AD1070', 'Sham', '19', '80', '80')
obj2.get_details()