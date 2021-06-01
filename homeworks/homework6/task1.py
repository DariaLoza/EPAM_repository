"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    """This decorator adds 2 methods to the class"""

    class Counter(cls):
        instances: int = 0

        @classmethod
        def counter(cls):
            if "instances" not in cls.__dict__:
                cls.instances = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__class__.instances += 1

        @classmethod
        def get_created_instances(cls):
            return cls.instances

        @classmethod
        def reset_instances_counter(cls):
            try:
                return cls.instances
            finally:
                cls.instances = 0

    return Counter


@instances_counter
class User:
    pass
