
#This program calculates the area of a parallelogram


import math

a = 13
b = 5
alfa = 30

def obliczpolerownolegloboku(a, b, alfa):
    alfarad = (alfa * 2 * math.pi)/360
    pole = math.sin(alfarad) * a * b
    print(pole)

obliczpolerownolegloboku(a, b, alfa)