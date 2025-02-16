
class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance method
    def get_info(self):
        print(f"{self.name} {self.gpa}")

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def getr_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"
    

    
student1 = Student("Mia", 3.5)
student2 = Student("Žiga", 4.0)
student3 = Student("Jan", 2.3)

print(Student.get_count())
print(Student.getr_average_gpa())