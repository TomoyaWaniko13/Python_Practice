class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(f'{self.name} + {self.age}')


class Student(Person):
    pass


student = Student('neko', 2)
student.printname()
x = Person('Joe', 10)
x.printname()

