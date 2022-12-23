import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start)
        return res
    return wrapper

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

@timer
def perform(n):
    return factorial(n)

print(perform(10))