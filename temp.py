"""Модуль для отработки учебного кода"""

from random import randint


class ParentClass:
    """Класс для демонстрации декоратора @classmethod"""

    value: list = []

    def __init__(self) -> None:
        pass

    @classmethod
    def update_value(cls, new_value):
        """Метода для обновления значения value"""
        cls.value.append(new_value)
        if cls.value[0] != cls.value[-1]:
            cls.value.pop(0)


class DaughterClass1(ParentClass):
    """Дочерний класс 1"""


class DaughterClass2(ParentClass):
    """Дочерний класс 2"""


object1 = DaughterClass1()
object2 = DaughterClass2()

print(object1.value, object2.value)
for _ in range(3):
    temp = randint(0, 100)
    object1.update_value((temp, temp + 1))
    print(object1.value, object2.value)
