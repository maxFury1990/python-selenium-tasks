import logging


def lru_cache_with_log(log=False):
    cache = {}

    def inner_function(function):
        def wrapper(number):
            if number in cache:
                if log:
                    print(f'found {number} in cache')
                return cache[number]
            cache[number] = function(number)
            return cache[number]
        return wrapper
    return inner_function


@lru_cache_with_log(log=True)
def factorial(n):
    logging.info("number less than 2 it does factorial equation")
    if n < 2:
        return 1
    return factorial(n - 1) * n


def test_factorial_numbers():
    print(factorial(5))
    print(factorial(3))
    print(factorial(8))