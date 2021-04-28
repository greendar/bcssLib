

"""Sample object template made for testing files

"""

class Student:
    def __init__(self, name, age, studNumber):
        self.name = name
        self.age = age
        self.studNumber = studNumber


    def __str__(self):
        return f"Name {self.name}, Age: {self.age}, Student Number: {self.studNumber}"
