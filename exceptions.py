# -*- coding: utf-8 -*-


class ZeroDerivativeException(Exception):
    #Raised when derivative equals zero in Newton method
    pass

class MaximumNumberOfIterationsException(Exception):
    #Raised when newtons method reaches maximum number of iterations
    pass

class BisectionFailException(Exception):
    #Raised when bisection method fails
    pass

class SecantFailException(Exception):
    #Raised when secant method fails
    pass
