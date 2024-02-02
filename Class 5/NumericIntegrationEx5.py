"""
Program that calculates the numeric value of an integral using the rectangle method
"""

granicadol = 0
granicagora = 5

def f(x):
    return 2*(x**3)+4*(x**2)-12*(x)

def oblicz(a, b, n):
    calka = 0
    a = float(a)
    b = float(b)
    n = float(n)
    
    i = (b-a)/n

    x0 = a
    xn = a+i

    while (a<=(xn)<=b) or (a>=(xn)>=b):
        pole=f((x0+(xn))/2)*i
        calka += pole

        x0 += i
        xn += i
    
    return calka

print("calka=" , oblicz(granicadol, granicagora, 100))