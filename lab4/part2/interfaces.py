from abc import ABC, abstractmethod


class ICourse(ABC):

    @property
    @abstractmethod
    def name(self):
        raise NotImplemented

    @property
    @abstractmethod
    def teacher(self):
        raise NotImplemented

    @property
    @abstractmethod
    def topics(self):
        raise NotImplemented

    @name.setter
    @abstractmethod
    def name(self, name):
        raise NotImplemented

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher):
        raise NotImplemented

    @topics.setter
    @abstractmethod
    def topics(self, topics):
        raise NotImplemented

    @abstractmethod
    def add_topic(self, topic):
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
        raise NotImplemented

    @property
    @abstractmethod
    def courses(self):
        raise NotImplemented

    @name.setter
    @abstractmethod
    def name(self, name):
        raise NotImplemented

    @courses.setter
    @abstractmethod
    def courses(self, courses):
        raise NotImplemented

    @abstractmethod
    def add_course(self, course):
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
        raise NotImplemented


class ITeacherFactory(ABC):

    @abstractmethod
    def __init__(self):
        raise NotImplemented

    @abstractmethod
    def create_teacher(self, name, courses):
        raise TypeError
