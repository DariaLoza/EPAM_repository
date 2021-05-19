from homeworks.homework5.task1 import Student, Teacher


def test_task_1():
    if __name__ == "__main__":
        teacher = Teacher("Daniil", "Shadrin")
        student = Student("Roman", "Petrov")
        assert teacher.last_name == "Shadrin"
        assert student.first_name == "Roman"
        expired_homework = teacher.create_homework("Learn functions", 0)
        assert expired_homework.created == "2021-05-17 16:34:23.323787"
        assert expired_homework.deadline == "0:00:00"
        assert expired_homework.text == "Learn functions"
        # create function from method and use it
        create_homework_too = teacher.create_homework
        oop_homework = create_homework_too("create 2 simple classes", 5)
        assert oop_homework.deadline == "5 days, 0:00:00"
        assert student.do_homework(oop_homework) == "You are late" "None"
        assert student.do_homework(expired_homework) == "You are late" "None"
