

import time

def my_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step

print(list(my_range(1, 15, 2)))


def fibonacci_num(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci_num(10)))


def odd_numbers(n):
    for i in range(1, n+1, 2):
        yield i

print(list(odd_numbers(10)))


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_t = time.time()
        result = func(*args, **kwargs)
        end_t = time.time()
        print(f'Funksiyani bajash vaqti: {end_t - start_t:.4f}')
        return result
    return wrapper

@timing_decorator
def timing(n):
    return sum(range(n))

timing(2000000)


def validate_age(func):
    def wrapper(age):
        if age < 0:
            raise ValueError('Yosh manfiy bolishi mumkin emas')
        return func(age)
    return wrapper

@validate_age
def ages(age):
    print(f'Yosh: {age}')

ages(18)
