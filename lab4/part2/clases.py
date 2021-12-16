from interfaces import ICourse, ILocalCourse, ICourseFactory, ITeacherFactory, IOffsiteCourse, ITeacher
from database import Connector


class Teacher(ITeacher):
    """
    Class contains teacher name and his courses
    implements ITeacher interface

    :param name: The name of teacher
    :param courses: Courses that head by teacher
    """
    def __init__(self, name, courses=[]):
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
    """
    Class implement course logics
    Class implement ICourse interface

    :param name: Name of course
    :param teacher: Name of teacher
    :param topics: topics of course
    """

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
            raise TypeError("teacher is not Teacher object")
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
    """
    Class contain information about local course
    Implements Cource, ILocalCourse
    """

    def __init__(self, name, teacher, *args):
        super().__init__(name, teacher, *args)

    def __str__(self):
        return f"Local course ->  Name: {self.name}, teacher: {self.teacher}, topics: {self.topics}."


class OffsiteCourse(Course, IOffsiteCourse):
    """
    Class contain information about offsite course
    Implements Cource, ILocalCourse
    """

    def __init__(self, name, teacher, *args):
        super().__init__(name, teacher, *args)

    def __str__(self):
        return f"Offsite course ->  Name: {self.name}, teacher: {self.teacher}, topics: {self.topics}."


class TeacherFactory(ITeacherFactory):

    def __init__(self):
        self.__connector = Connector.connect()

    def create_teacher(self, name, *courses):
        """
        Create teacher and save it
        :return teacher
        :raise SQLError
        """

        teacher = Teacher(name, *courses)
        insert_query = f"INSERT INTO teacher (name) VALUES (%s) "
        with self.__connector.cursor() as cursor:
            cursor.execute(insert_query, (teacher.name, ))
            self.__connector.commit()
        return teacher


class CourseFactory(ICourseFactory):

    def __init__(self):
        self.__connector = Connector.connect()

    def create_course(self, place, name, teacher, *args):
        """
        Create and return course
        save course in database
        :returns course
        :raise SLQError
        """
        if place == "local":
            course = LocalCourse(name, teacher, *args)
        if place == "offsite":
            course = OffsiteCourse(name, teacher, *args)
        insert_query = f"INSERT INTO course(name, teacher, topics) " \
                       f"VALUES(%s,(SELECT id FROM teacher WHERE name = %s), %s)"
        with self.__connector.cursor() as cursor:
            cursor.execute(insert_query, (course.name, course.teacher.name, ', '.join(course.topics)))
            self.__connector.commit()
        return course
