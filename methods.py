# -*- coding: utf-8 -*-

from sympy import *
from exceptions import *

x = Symbol('x')

def newtons_method(f, x0, maxn, epsilon):
    xn = N(x0)
    fdiff = f.diff(x)
    for n in range(0, maxn):
        if(N(abs(f.subs(x, xn)))<epsilon):
            return round(N(xn), 10);
        if(N(fdiff.subs(x, xn))==0):
            raise ZeroDerivativeException
            return None
        xn = N(xn-N(f.subs(x, xn))/N(fdiff.subs(x, xn)))
    raise MaximumNumberOfIterationsException
    print("abcd")
    
def secant_method(f, a, b, iterations):
    if f.subs(x, N(a))*f.subs(x, N(b)) >= 0:
        raise SecantFailException
        return None
    a_n = N(a)
    b_n = N(b)
    for n in range(1,iterations+1):
        m_n = a_n - f.subs(x, a_n)*(b_n - a_n)/(f.subs(x, b_n) - f.subs(x, a_n))
        f_m_n = f.subs(x, m_n)
        if f.subs(x,a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f.subs(x, b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            return m_n
        else:
            raise SecantFailException
            return None
    return a_n - f.subs(x, a_n)*(b_n - a_n)/(f.subs(x, b_n) - f.subs(x, a_n))

def bisection_method(f, a, b, iterations):
    if f.subs(x, N(a))*f.subs(x, N(b)) >= 0:
        raise BisectionFailException
        return None
    a_n = N(a)
    b_n = N(b)
    for n in range(1,iterations+1):
        m_n = (a_n + b_n)/2
        f_m_n = f.subs(x, m_n)
        if f.subs(x, a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f.subs(x, b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            return m_n
        else:
            raise BisectionFailException
            return None
    return (a_n + b_n)/2






