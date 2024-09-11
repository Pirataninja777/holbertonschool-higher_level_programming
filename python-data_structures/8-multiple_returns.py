#!/usr/bin/python3
def multiple_returns(sentence):
    # Si la cadena está vacía, devolvemos la longitud
    # y None como primer carácter
    if sentence == "":
        return (0, None)
    else:
        # Devolver una tupla con la longitud de la cadena
        # y el primer carácter
        return (len(sentence), sentence[0])
