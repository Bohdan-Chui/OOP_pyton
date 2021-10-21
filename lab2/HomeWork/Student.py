class Student:
    __slots__ = ['name', 'surname', 'record_book_number', 'grades']

    __count = 0

    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades
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
            raise TypeError('grades must be of type dict')
        if any(not isinstance(key, str) for key in grades.keys()):
            raise TypeError('grade\'s key must be of type str')
        if any(not isinstance(value, int) for value in grades.values()):
            raise TypeError('grade\'s value must be of type int')
        if any(value < 0 or value > 100 for value in grades.values()):
            raise ValueError('grade must be in range(0, 101)')
        self.__grades = grades

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __str__(self) -> str:
        return f'Student [ name = {self.name}, surname = {self.surname}, grades = {self.grades}]'


