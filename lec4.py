# class StudentStruct:
#     def __init__(self, name, id, gpa):
#         self.name = name
#         self.id = id
#         self.gpa = gpa

# s1 = StudentStruct("Ali", 123, 3.5)
# print(s1.name, s1.id, s1.gpa)

class Student:
    def __init__(self, name, id, gpa):
        self.name = name
        self.id = id
        self.gpa = gpa

    def promote(self):
        self.gpa += 0.5

    def info(self):
        print(f"{self.name} - {self.id} - {self.gpa}")

# s1 = Student("Ali", 123, 3.5)
# s1.promote()
# s1.info()

class Car:
    def __init__(self, model, year, mileage):
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance):
        self.mileage += distance

    def info(self):
        print(f"{self.model} - {self.year} - {self.mileage} km")