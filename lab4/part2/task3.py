from clases import TeacherFactory, CourseFactory
if __name__ == '__main__':

    teacherFactory = TeacherFactory()
    teacher = teacherFactory.create_teacher("myhailo")

    courseFactory = CourseFactory()
    cource = courseFactory.create_course("local", "computerCourse", teacher, "Monitor", "Mouse")
    print(cource)

    teacher.add_course(cource.name)
    print(teacher)
