"""
Program that solves the birthday problem
"""



import random as rn
#debug array to check if the first function that checks for the same elements in an array works
debugarray = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]


#function to check if there are at least two of the same element in an array
def sprawdz(lista):
    for x in lista:
        for h in range(len(lista)):
            if lista.index(x) != h:
                if x == lista[h]:
                    return True
    
    return False
#function that calcualtes the probability (approx) of two people having the same birthday
def paradoks(ilosc_uczniow, dokladnosc):
    iloscok = 0
    for h in range(dokladnosc):
        templista = []
        #create the class of people
        for i in range(ilosc_uczniow):
            data = rn.randint(1, 365)
            templista.append(data)
        #check if two people have the same date in class    
        if sprawdz(templista):
            iloscok += 1
    #return probability
    return (iloscok/dokladnosc) 

print("Sprawdzamy czy funkcja prawidlowo działa:", sprawdz(debugarray))
print("umieść dokładność z jaką chcesz obliczyc prawdopodobieństwo, że dwie osoby mają taką samą date urodzin")
g = input()
print("Prawdopodobieństwo wynosi:",paradoks(17, int(g)))