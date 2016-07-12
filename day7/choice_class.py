#!/usr/bin/env python3
# Author: Zhangxunan
import pickle


class Teacher:
    """
    老师类
    """
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.assets = 0

    def teach_event(self):
        """
        教学事故
        :return:None
        """
        self.assets -= 100

    def attend_class_fee(self, salary):
        """
        上课费
        :param salary:上课的工资
        :return: None
        """
        self.assets += salary

    def show_info(self):
        print('创建了%s老师，%s老师，%d岁，爱好%s' % (self.name, self.name, self.age, self.hobby))

    def show_assets(self):
        print('%s的资产是%d元' % (self.name, self.assets))


class Course:
    """
    课程类
    """
    def __init__(self, course, fee, teacher):
        self.course = course
        self.fee = fee
        self.teacher = teacher

    def attend_class(self):
        self.teacher.attend_class_fee(self.fee)
        content = '已经学习 %s' % self.course
        self.teacher.show_assets()
        return content

    def show_info(self):
        print('创建了%s课程，课时费为%d,任课老师为%s' % (self.course, self.fee, self.teacher.name))


class Admin:
    """
    管理员类
    """
    def __init__(self):
        self.teacher_file_name = 'teacher.txt'
        self.course_file_name = 'course.txt'

    def create_teacher(self):
        teacher1 = Teacher('tom', 25, 'watch movie')
        teacher1.show_info()
        teacher2 = Teacher('jerry', 26, 'sports')
        teacher2.show_info()
        teacher3 = Teacher('jack', 30, 'play basketball')
        teacher3.show_info()
        teacher4 = Teacher('rose', 29, 'swimming')
        teacher4.show_info()
        teachers = [teacher1, teacher2, teacher3, teacher4]
        with open(self.teacher_file_name, 'wb') as f:
            pickle.dump(teachers, f)

    def create_course(self):
        with open(self.teacher_file_name, 'rb') as f:
            teachers = pickle.load(f)
        course1 = Course('Chinese', 100, teachers[0])
        course1.show_info()
        course2 = Course('Math', 150, teachers[1])
        course2.show_info()
        course3 = Course('English', 120, teachers[2])
        course3.show_info()
        course4 = Course('Physics', 200, teachers[3])
        course4.show_info()
        courses = [course1, course2, course3, course4]
        with open(self.course_file_name, 'wb') as f:
            pickle.dump(courses, f)


class Student:
    """
    学生类
    """
    def __init__(self, name, course_obj):
        self.name = name
        self.course_obj = course_obj

    def attend_class(self):
        content = self.course_obj.attend_class()
        print(self.name, content)


def main():
    admin = Admin()
    admin.create_teacher()
    admin.create_course()
    with open('course.txt', 'rb') as f:
        courses = pickle.load(f)
    student1 = Student('eric', courses[0])
    student1.attend_class()
    student2 = Student('james', courses[1])
    student2.attend_class()
    student3 = Student('alex', courses[2])
    student3.attend_class()
    student4 = Student('Yao', courses[3])
    student4.attend_class()


if __name__ == '__main__':
    main()

