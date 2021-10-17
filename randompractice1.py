class Student:
  def __init__(self,name, set_age, set_marks):
   self.name = name
   self.age = set_age
   

  def set_age(self):
    self.age = int(input("What is student's age? "))
    print (self.age)
  def set_marks(self):
    self.set_marks = int(input("What mark was earned? "))
    print (self.set_marks)
student_1 = Student('John', 29, 88)
student_1.name
student_1.age
student_1.set_age()
student_1.set_marks()
