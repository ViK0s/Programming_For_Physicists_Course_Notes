

"""
Program that calculates the max and min of a function, and finds where the value of the function equals 0
"""




#defining arrays which have from top: 
#all the values possible
#all the values of x which result in f(x) = 0 (approx)
lista = []
listazer = []


#defining mathematical function
def f(x):
    return (x**4)+5*(x**3)-20*(x**2)+1


def oblicz(poczatek:int, koniec:int):
    #check if the beginning of the range of numbers is higher than the end, if it is,
    #print to user and escape the function
    
    if poczatek > koniec:
        print("koniec większy od początku")
        return
    
    
    #temp vars
    
    listatemp = []
    i = poczatek
    a = 0
    b = 0
    while koniec > i:
        i += 0.1
        lista.append(f(i))
        #print(lista[-1]) #easy debugging for array
        #znajdź miejsca zerowe funkcji (przybliżone)
        if int(lista[a]) == 0:
            listazer.append(round(i, 2))
            listatemp.append(listazer[b]) 
            b += 1
        a += 1
    print("Liczby dla których funkcja przyjmuje wartość zerową:\n",listatemp)
    
    maxl = None
    minl = None
    #check for the local maximum and minimum
    for h in range(len(lista) - 1):
        if h >= 1 and h != len(lista):
            if lista[h] > lista[h-1] and lista[h] > lista[h+1]:
                maxl = lista[h]
                print("Maximum lokalne:", maxl)
            elif lista[h] < lista[h-1] and lista[h] < lista[h+1]:
                minl = lista[h]
                print("Minimum lokalne:",minl)
    #if min or max not found, print to user
    if maxl == None:
        print("brak maximum lokalnego")
    elif minl == None:
        print("brak minimum lokalnego")
    return
    

print("Podaj początek przedziału liczb dla którego chcesz wyznaczyc min i max oraz miejsca zerowe")
x = input()
print("Podaj koniec przedziału")
y = input()
try:
    oblicz(int(x), int(y))
except:
    print("Podano nieprawidłowe dane")
