# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from methods import *
from exceptions import *

def solve_newton():
    x0 = float(input("Podaj x początkowe: \n x0="))
    maxn = int(input("Podaj maksymalną liczbę iteracji:\n maxN="))
    epsilon = float(input("Podaj maksymalny bład względny:\n epsilon="))
    try:
        global solution
        solution = newtons_method(y, x0, maxn, epsilon)
    except(ZeroDerivativeException):
        print("Podczas wykonywania algorytmu pochodna funkcji wyniosła zero.\n Wypróbuj inne miejsce startowe lub inną metodę.")
        main()
        
    except(MaximumNumberOfIterationsException):
        print("Osiągnięto maksymalną liczbę iteracji. Spróbuj zmienić parametry startowe lub skorzystać z innej metody.")
        main()
        
def solve_bisection():
    print("Podaj przedział początkowy [a, b] oraz maksymalną liczbę iteracji. \n Dla zwiększenia dokładnosci podaj większą liczbę iteracji.")
    a = float(input("a="))
    b = float(input("b="))
    iterations = int(input("Maksymalna liczba iteracji: "))
    try:
        global solution
        solution = bisection_method(y, a, b, iterations)
    except(BisectionFailException):
        print("Metoda siecznych zawiodła. Upewnij się, że f(a)*f(b)<= 0, czyli mają różne znaki lub wybierz inną metodę.")
        main()
        
def solve_secant():
    print("Podaj przedział początkowy [a, b] oraz maksymalną liczbę iteracji. \n Dla zwiększenia dokładnosci podaj większą liczbę iteracji.")
    a = float(input("a="))
    b = float(input("b="))
    iterations = int(input("Maksymalna liczba iteracji: "))
    try:
        global solution
        solution = secant_method(y, a, b, iterations)
    except(SecantFailException):
        print("Metoda sekansów zawiodła. Upewnij się, że f(a)*f(b)<= 0, czyli mają różne znaki lub wybierz inną metodę.")
        main()
        
def show_graph():
    t = np.arange(solution-10, solution+10, 0.01)
    ys = [y.subs(x, ti) for ti in t]
    plt.plot(t, ys, color="black")
    plt.plot(solution, y.subs(x, solution), "g*")
    plt.grid(True)
    plt.show()

def main():
    n = 0
    x = Symbol('x')
    
    global y
    
    y = sympify(0)
    
    while(n not in range(1, 4)):
        n = int(input("Wybierz metodę: \n [1] Metoda Newtona \n [2] Metoda siecznych \n [3] Metoda sekansów \n"))
        if(n not in range(1,4)):
            print("Błąd. Wybierz jedną z dostępnych metod.")
    
    while(x not in y.free_symbols):
        y = sympify(input("Podaj wzór funkcji: \n f(x)="))
        if(x not in y.free_symbols):
            print("Błąd. Podaj prawidłowy wzór funkcji.")
        
    if(n == 1):
        solve_newton()
    if(n == 2):
        solve_bisection()  
    if(n == 3):
        solve_secant()
    
    
    

main()

if(solution!=None):
   print("Rozwiązanie to x="+str(solution))
   show_graph()
else:
    print("Nie zdołano znaleźć rozwiązania za pomocą zadanych parametrów. Spróbuj jeszcze raz.")
    main()





