import functools
import time

#   timer decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start)
        return res
    return wrapper

#   factorial calculation using recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

#   fibonachi number calculation using recursion
def fibbo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = fibbo(n-1)
    b = fibbo(n-2)
    return a+b

#   performing function
@timer
def perform(n):
    return factorial(n), fibbo(n)

print(perform(30))