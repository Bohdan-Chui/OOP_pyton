from Student import  Student

class Group:

    def __init__(self, students):


    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, students):
        if not isinstance(students, Student):
            raise TypeError('students have to be Student type')
        else: self.__students = students

