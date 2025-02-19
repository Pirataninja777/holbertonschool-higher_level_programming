#!/usr/bin/env python3

class SwimMixin:
    """Mixin que agrega la capacidad de nadar."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin que agrega la capacidad de volar."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Clase Dragon que puede nadar, volar y rugir."""
    def roar(self):
        print("The dragon roars!")


if __name__ == "__main__":
    # Prueba de la clase Dragon
    dragon = Dragon()
    dragon.swim()  # The creature swims!
    dragon.fly()   # The creature flies!
    dragon.roar()  # The dragon roars!
