#!/usr/bin/python3
class Student:
    """Define un estudiante con: primer/segundo nombre y edad """

    def __init__(self, first_name, last_name, age):
        """iniciamos instancia con atributos"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retorna un diccionario de la instancia Estudiante"""
        return self.__dict__
