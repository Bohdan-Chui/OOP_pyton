"""
    This class implement student entity
    STUDENT contains the student's name, surname, record book number and grades.
"""

class Student:

    __count = 0

    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = dict(grades)
        Student.__count += 1

    @classmethod
    def student_count(cls):
        return Student.__count

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if name and name.strip():
            self.__name = name
        else:
            raise TypeError("name customer is empty")

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("surname must be a string")
        if surname and surname.strip():
            self.__surname = surname
        else:
            raise TypeError("surname is empty")

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if not isinstance(grades, dict):
            raise TypeError('Grades must be dict type')
        if not any(isinstance(key, str) for key in grades.keys()):
            raise TypeError('Keys must be str type')
        if not any(isinstance(value, int) for value in grades.values()):
            raise TypeError('Values must be int type')
        self.__grades = grades

    def get_average(self):
        return sum(self.__grades.values()) / len(self.__grades)

    def __eq__(self, other):
        if isinstance(other, Student):
            return (self.name, self.surname) == (other.name, other.surname)
        return  False

    def __str__(self) -> str:
        return f'Student [ name = {self.name}, surname = {self.surname}, grades = {self.grades}]'

    def __hash__(self) -> int:
        return hash(self.name) + hash(self.surname)


