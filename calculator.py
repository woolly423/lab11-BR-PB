#https://github.com/woolly423/lab11-BR-PB
#Partner 1: Brett Raimann
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# <<<<<<< HEAD
import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a

def logarithm(a,b):
    if a <= 0 or b <= 0:
        raise ValueError
    else:
        return math.log(b,a)
    
def exp(a,b):
    return math.pow(a,b)
# =======
# First example
def add(a, b):
   return a + b
# >>>>>>> 2b81feb91232d2a1b11ce1d5600d764927fa9ef4

# def sub(a, b):
#    return a - b
#
#
# def mul(a, b):
#    return a * b
#
#
# def div(a, b):
#    if a == 0:
#        raise ZeroDivisionError
#    return b / a
#
#
# def log(a, b):
#    if b <= 0 or a <= 0:
#        raise ValueError
#    return math.log(b, a)
#
# def exp(a, b):
#    return a**b

