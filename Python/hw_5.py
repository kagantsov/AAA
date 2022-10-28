import json
from typing import Iterator
from keyword import iskeyword
import functools


class PythonAttribute:
    """Класс, который преобразует формат JSON"""

    @staticmethod
    def make_attribute(json_item: Iterator) -> object:
        """Метод, который принимает json_item, а возвращает dict/list"""
        if isinstance(json_item, dict):
            obj = type('object', (object,), {})
            for key, value in json_item.items():
                setattr(obj, key, PythonAttribute.make_attribute(value))
            return obj
        elif isinstance(json_item, list):
            list_attribute = []
            for element in json_item:
                list_attribute.append(PythonAttribute.make_attribute(element))
            return list_attribute
        else:
            return json_item


class ColorizeMixin:
    """Окрашивает текст в заданыный цвет"""
    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        cls.__repr__ = cls._replace_repr(cls.__repr__)

    @classmethod
    def _replace_repr(cls, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            return f'\033[1;{str(cls.repr_color)};40m{text}\033[1;0;40m'
        return wrapper


class Advert(ColorizeMixin, PythonAttribute):
    """Класс, преобразующий вложенную структуру из JSON в словарь или список"""
    repr_color = 33

    def __init__(self, advert):
        super().__init__()
        self.price = 0
        self.title = ''
        for item in advert:
            item_name = item + '_' if iskeyword(item) else item
            setattr(self, item_name, PythonAttribute.make_attribute(advert[item]))

    def __repr__(self) -> str:
        return f'{self.title} | {self.price} ₽'

    @property
    def price(self) -> int:
        """Геттер для параметра "цена". Если цена не установлена - устанавливает 0 по умолчанию"""
        return self.price

    @price.setter
    def price(self, price):
        """Сеттер для параметра "цена". Если цена меньше 0 - выводит ошибку"""
        if price >= 0:
            self._price = price
        else:
            raise ValueError('Цена должна быть >= 0')


if __name__ == '__main__':
    lesson_str1 = """{
        "title": "iPhone X",
        "price": 100,
        "location": {
        "address": "город Самара, улица Мориса Тореза, 50",
        "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }"""

    lesson1 = json.loads(lesson_str1)
    lesson_ad1 = Advert(lesson1)
    print(lesson_ad1.location.metro_stations)

    lesson_str2 = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""

    lesson2 = json.loads(lesson_str2)
    lesson_ad2 = Advert(lesson2)
    print(lesson_ad2.class_)

    lesson_str3 = """{
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }"""
    lesson3 = json.loads(lesson_str3)
    lesson_ad3 = Advert(lesson3)
    print(lesson_ad3.location.address)




