# Design a class that stores the information of a student and displays the same.

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Roll number:", self.roll_no)
        print("Marks:", self.marks)

s1 = Student("Sundaram", 127, 99)
s1.display()            

       
