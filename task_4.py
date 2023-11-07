class Student:
    def __init__(self, first_name, last_name, course):
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.grades = []

    def add_grade(self, grade):
        if isinstance(grade, int) and 1 <= grade <= 10:
            self.grades.append(grade)
        else:
            print("Неверный формат оценки")

    def get_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return None

    @staticmethod
    def is_valid_name(name):
        return name.isalpha() or name.replace(" ", "").isalpha()

    @classmethod
    def from_string(cls, string):
        first_name, last_name, course = string.split(",")
        if cls.is_valid_name(first_name) and cls.is_valid_name(last_name):
            course = int(course)
            return cls(first_name, last_name, course)
        else:
            print("Неверный формат данных.")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course} курс - {self.get_average()} средний балл"
