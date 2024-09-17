#!/usr/bin/python3
import sys


def main():
    argumento = len(sys.argv) - 1
    if argumento == 0:
        print(f"{argumento} arguments.")
    elif argumento == 1:
        print(f"{argumento} argument:")
    else:
        print(f"{argumento} arguments:")

    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")


if __name__ == "__main__":
    main()
