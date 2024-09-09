#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    # abs()devuelve numero absoluto convierte negativo en positivo
    print(last_digit, end="")
    return last_digit
