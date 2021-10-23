"""
    This class implement group entity
"""

from Student import  Student

class Group:

    def __init__(self, *students):
        self.__numberOfStudents = 20
        self.students = students

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, students):
        students = list(students)
        if not all(isinstance(student, Student) for student in students):
            raise TypeError('Students must be a list of Studens')
        if not (len(set(students)) == len(students)):
            raise TypeError('Students must be unique')
        if len(students) >= self.__numberOfStudents:
            raise ValueError('a lot of students')
        self.__students = list(students)

    def add_students(self, student):
        students = list(student)
        if not all(isinstance(student, Student) for student in students):
            raise TypeError('Students must be a list of Studens')
        if not (len(set(students)) == len(students)):
            raise TypeError('Students must be unique')
        if not (len(set(students)) == len(self.__students)):
            raise TypeError('student is alresdy in class')
        if not (self.__students.len + students.len >= self.__numberOfStudents):
            raise ValueError('a lot of students')
        self.__students.append(student)

    def highest_average_score(self, number_of_students):
        self.__students.sort(key=lambda x: x.get_average(), reverse=True)
        return self.__students[:number_of_students]