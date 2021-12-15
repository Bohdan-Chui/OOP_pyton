from Clases import TeacherFactory, CourseFacroty
if __name__ == '__main__':

    teacherFactory = TeacherFactory()
    teacher = teacherFactory.createTeacher("myhailo")

    courseFactory = CourseFacroty()
    cource = courseFactory.createCourse("local", "computerCourse", teacher, "Monitor", "Mouse")
    print(cource)

    teacher.add_course(cource.name)
    print(teacher)
