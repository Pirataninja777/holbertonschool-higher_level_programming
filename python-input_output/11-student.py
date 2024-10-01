#!/usr/bin/python3
"""Crea la clase Estudiante"""


class Student:
    """Define un estudiante por su nombre, apellido y edad"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Devuelve un diccionario de la representación del estudiante"""
        if attrs is None:
            return self.__dict__
        # Si attrs es una lista de strings
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: self.__dict__[attr] for attr in attrs if attr in self.__dict__}

        return {}

    def reload_from_json(self, json):
        """Reemplaza todos los atributos del estudiante con valores de json"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
