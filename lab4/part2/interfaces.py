from abc import ABC, abstractmethod


class ICourse(ABC):

    @property
    @abstractmethod
    def name(self):
        """name getter"""
        raise NotImplemented

    @property
    @abstractmethod
    def teacher(self):
        """teacher getter"""
        raise NotImplemented

    @property
    @abstractmethod
    def topics(self):
        """topics getter"""
        raise NotImplemented

    @name.setter
    @abstractmethod
    def name(self, name):
        """name setter"""
        raise NotImplemented

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher):
        """teacher setter"""
        raise NotImplemented

    @topics.setter
    @abstractmethod
    def topics(self, topics):
        """topics setter"""
        raise NotImplemented

    @abstractmethod
    def add_topic(self, topic):
        """add topic in course"""
        raise NotImplemented

    @abstractmethod
    def __str__(self):
        raise NotImplemented

    @abstractmethod
    def __init__(self, name, teacher, *args):
        raise NotImplemented


class ITeacher(ABC):

    @property
    @abstractmethod
    def name(self):
        """name getter"""
        raise NotImplemented

    @property
    @abstractmethod
    def courses(self):
        """courses getter"""
        raise NotImplemented

    @name.setter
    @abstractmethod
    def name(self, name):
        """name setter"""
        raise NotImplemented

    @courses.setter
    @abstractmethod
    def courses(self, courses):
        """courses setter"""
        raise NotImplemented

    @abstractmethod
    def add_course(self, course):
        """function add course to teacher"""
        raise NotImplemented

    @abstractmethod
    def __str__(self):
        raise NotImplemented


class ILocalCourse(ABC):

    @abstractmethod
    def __str__(self):
        raise NotImplemented

    @abstractmethod
    def __init__(self, name, teacher, *args):
        raise NotImplemented


class IOffsiteCourse(ICourse):

    @abstractmethod
    def __str__(self):
        raise NotImplemented

    @abstractmethod
    def __init__(self, name, teacher, *args):
        raise NotImplemented


class ICourseFactory(ABC):

    @abstractmethod
    def __init__(self):
        raise NotImplemented

    @abstractmethod
    def create_course(self, place, name, teacher, *args):
        """
        Create and return course
        save course in database
        """
        raise NotImplemented


class ITeacherFactory(ABC):

    @abstractmethod
    def __init__(self):
        raise NotImplemented

    @abstractmethod
    def create_teacher(self, name, courses):
        """
               Create teacher and save it
        """
        raise TypeError
