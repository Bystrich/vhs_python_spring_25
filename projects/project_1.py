# Schreibe ein Programm, mit dem du zwei (ganze) Zahlen addieren, multiplizieren, subtrahieren oder
# dividieren kannst. Schreibe das Programm so, dass nach dem Ausgeben des Ergebnisses gefragt wird,
# ob eine weitere Rechnung gemacht werden soll!

import math


def square_root(x):
    if x < 0:
        return "Es kann nicht die wurzel von einer Zahl kleiner als 0 gezogen werden!"
    else:
        return math.sqrt(x)

print(square_root(3))



