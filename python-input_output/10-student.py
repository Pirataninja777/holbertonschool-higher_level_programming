#!/usr/bin/python3
"""crea clase Estudiante"""


class Student:
    """Lo mismo edad, primero y segundo nombre"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self. __dict__

        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs
        ):
            return {
                    attr: self.__dict__[attr]
                    for attr in attrs if attr in self.__dict__
            }

        return {}
