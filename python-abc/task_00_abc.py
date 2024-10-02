#!/usr/bin/python3
"""Este modulo crea una clase abstracta Animal
y subclases"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Clase abstracta Animal implementado por subclases"""
    @abstractmethod
    def sound(self):
        """retorna sonido de animal"""
        pass


class Dog(Animal):
    """sub clase Perro"""
    def sound(self):
        return "bark"


class Cat(Animal):
    """subclase Gato"""
    def sound(self):
        return "meow"
