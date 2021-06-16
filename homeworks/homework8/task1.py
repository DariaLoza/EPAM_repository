from collections import namedtuple
import functools

# типичный паттерн класс-декоратор
"""class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num = 0

    def __call__(self, *args, **kwargs):
        self.num += 1
        print(f'Вызов {self.func.__name__!r}: {self.num}')
        return self.func(*args, **kwargs)

@CountCalls
def say(name):
    print(f'Привет {name}')"""

"""with open('key_value_storage', 'r', encoding='utf') as file:  # Читаем файл
    data = file.read().splitlines()  # read().splitlines() - чтобы небыло пустых строк
print(data)
dic = {}  # Создаем пустой словарь

for line in data:  # Проходимся по каждой строчке
    key, value = line.split('=')  # Разделяем каждую строку по двоеточии(в key будет - пицца, в value - 01)
    dic.update({key: value})  # Добавляем в словарь

print(dic)  # Вывод словаря на консоль

list_of_keys = []
for key in dic:
    list_of_keys.append(key)
print(list_of_keys)
result = namedtuple('result', list_of_keys)
storage = result(**dic)
storage2 = storage._asdict()
print(result)
print(storage)
print(storage.song)
print(storage._asdict()['name'])
print(storage2['name'])"""


class KeyValueStorage:
    def __init__(self, path):
        with open(path, "r") as file:
            data = file.read().splitlines()

            for line in data:
                key, value = line.split("=")

                if not key.isidentifier():
                    raise ValueError("Wrong key!")

                if value.isdigit():
                    value = int(value)

                if key not in self.__dict__:
                    setattr(self, key, value)

    def __getitem__(self, key):
        return self.__dict__.get(key, None)



storage = KeyValueStorage('key_value_storage')
print(storage["name"])
print(storage.song)
print(storage.power)
