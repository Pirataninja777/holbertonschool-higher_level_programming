#!/usr/bin/env python3

class Fish:
    """Clase Fish con métodos para nadar y definir su hábitat."""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Clase Bird con métodos para volar y definir su hábitat."""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Clase FlyingFish que hereda de Fish y Bird."""
    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    # Prueba de la clase FlyingFish
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()

    # Mostrar el método de resolución de orden (MRO)
    print(FlyingFish.mro())
