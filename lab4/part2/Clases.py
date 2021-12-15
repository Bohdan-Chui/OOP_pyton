from Interfaces import ICourse, ILocalCourse, ICourseFactory,ITeacherFactory, IOffsiteCourse, ITeacher
from Database import Connector

class Teacher(ITeacher):

    def __init__(self, name, courses = []):
        self.name = name
        self.courses = courses

    @property
    def name(self):
        return self.__name

    @property
    def courses(self):
        return self.__courses

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if name and name.strip():
            self.__name = name
        else:
            raise TypeError("name teacher is empty")

    @courses.setter
    def courses(self, courses):
        if not isinstance(courses, list):
            raise TypeError("courses must be list type")
        if any(not isinstance(course, Course) for course in courses):
            raise TypeError("not course type")
        self.__courses = courses

    def add_course(self, course):
        if not isinstance(course, Course):
            raise TypeError("not course type")
        self.__courses.append(course)

    def __str__(self):
        return f"Teacher: {self.name}"

class Course(ICourse):

    def __init__(self, name, teacher, *args):
        self.name = name
        self.teacher = teacher
        self.topics = args

    @property
    def name(self):
        return self.__name

    @property
    def teacher(self):
        return self.__teacher

    @property
    def topics(self):
        return self.__topics

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be str")
        self.__name = name

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("teacher isnot Teacher object")
        self.__teacher = teacher

    @topics.setter
    def topics(self, topics):
        if any(not isinstance(topic, str) for topic in topics):
            raise TypeError("topic must be srt type")
        self.__topics = topics

    def add_topic(self, topic):
        if not isinstance(topic, str):
            raise TypeError("topic must be str type")
        self.__topics.append(topic)

    def __str__(self):
        return f"Course ->  Name: {self.name}, teacher: {self.teacher}, topics: {self.topics}."

class LocalCourse(Course, ILocalCourse):

    def __init__(self, name, teacher, *args):
        super().__init__(name, teacher, *args)

    def __str__(self):
        return f"Local course ->  Name: {self.name}, teacher: {self.teacher}, topics: {self.topics}."


class OffsiteCourse(Course, IOffsiteCourse):

    def __init__(self, name, teacher, *args):
        super().__init__(name, teacher, *args)

    def __str__(self):
        return f"Offsite course ->  Name: {self.name}, teacher: {self.teacher}, topics: {self.topics}."


class TeacherFactory(ITeacherFactory):

    def __init__(self):
        self.__connector = Connector.connect()

    def createTeacher(self, name, *courses):
        teacher = Teacher(name, *courses)
        insertQuery = f"INSERT INTO teacher (name) VALUES (%s) "
        with self.__connector.cursor() as cursor:
            cursor.execute(insertQuery, (teacher.name, ))
            self.__connector.commit()
        return teacher

class CourseFacroty(ICourseFactory):

    def __init__(self):
        self.__connector = Connector.connect()

    def createCourse(self, place, name, teacher, *args):
        if place == "local":
            course = LocalCourse(name, teacher, *args)
        if place == "offsite":
            course = OffsiteCourse(name, teacher, *args)
        insertQuery = f"INSERT INTO course(name, teacher, topics) VALUES(%s,(SELECT id FROM teacher WHERE name = %s), %s)"
        with self.__connector.cursor() as cursor:
            cursor.execute(insertQuery, (course.name, course.teacher.name, ', '.join(course.topics)))
            self.__connector.commit()
        return course

if __name__ == '__main__':

    teacherFactory = TeacherFactory()
    teacher = teacherFactory.createTeacher("myhailo")

    courseFactory = CourseFacroty()
    cource = courseFactory.createCourse("local", "computerCourse", teacher, "Monitor", "Mouse")
    print(cource)

    teacher.add_course(cource.name)
    print(teacher)




