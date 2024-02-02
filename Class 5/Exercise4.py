
"""
This program calculates, and checks if a Roman coin from the times of Nero could have been made if it's C14 concentration is 90%
For more accurate information check the exercise image
"""
import math

czaspol = 5730
czasmozliwy = 2023 - 54
przedzial = 68 - 54

def obliczlamb(tpol):
    lamb = math.log(2)/tpol
    print("lambda:", lamb)
    return lamb

def sprawdzprawde(lamb, czasmozliwy, przedzial):
    czas = -(math.log(9/10)/lamb)
    print("Obliczony czas:", czas, "lat")
    if czas < czasmozliwy or czas > czasmozliwy + przedzial:
        print("Nie jest to możliwe") 


sprawdzprawde(obliczlamb(czaspol), czasmozliwy, przedzial)