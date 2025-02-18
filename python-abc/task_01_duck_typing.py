#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Clase abstracta para figuras geometricas.
    """

    @abstractmethod
    def area(self):
        """
        Metodo abstracto para calcular area.
        Sera implentado por las clases derivadas.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Metodo abstracto para calcular el area de la forma.
        Debe ser implementado por las clases derivadas.
        """
        pass


class Circle(Shape):
    """
    Clase que representa un circulo,hereda de Shape
    """
    def __init__(self, radius):
        """
        Inicializa un circulo con un radio.
        :param radius: Radio del circulo (numero positivo).
        """
        self.radius = radius

    def area(self):
        """
        Calcula el area del circulo usando la formula radio al cuadrado
        :retorna: Area del circulo.
        """
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        """
        Calcula el perimetro (circunferencia) del circulo usando la formula.
        :return: Perimetro del circulo.
        """
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    Clase que representa un rectangulo, derivada de Shape.
    """
    def __init__(self, width, height):
        """
        Inicializa un rectangulo con un ancho y una altura.
        :param width: Ancho del rectangulo (numero positivo)
        :param height: Altura del rectangulo (numero positivo).
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calcula el area del rectangulo usando la formula ancho x altura
        :return: Area del rectangulo.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calcula el perimetro del rectangulo usando la
        formula 2(ancho + altura).
        :return: Perimetro del rectangulo.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Funcion que imprime el area y el perimetro de
    cualquier forma.
    Se basa en el duck typing el area,
    asumiendo que el objeto tiene los metodos de area y perimetro
    :param shape: Objeto que debe tener implementados los metodos
    area y perimeter
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
