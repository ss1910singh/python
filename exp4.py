#Satish singh

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id
    
  def display(self):
    print(f"ID: {self.id} \nName: {self.name}")

object = Employee("Satish", "1020")
object.display()


