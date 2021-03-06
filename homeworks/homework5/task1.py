"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""

from datetime import datetime, timedelta


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = timedelta(deadline)
        self.created = datetime.now()

    def is_active(self):
        return (self.deadline + self.created) > datetime.now()


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def do_homework(my_homework):
        if my_homework.is_active():
            return my_homework
        else:
            print("You are late")
            return None


class Teacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)


if __name__ == "__main__":
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    teacher.first_name  # Daniil
    student.last_name  # Petrov

    expired_homework = teacher.create_homework("Learn functions", 0)
    expired_homework.created  # Example:
    expired_homework.deadline
    expired_homework.text

    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
