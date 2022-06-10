# This is a sample Python script.
import time
import functools
import sys
import numpy as np

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
sys.setrecursionlimit(10 ** 9)

def find_squares_opt(array):
    arr = np.array(array)
    return arr**2+1


def find_squares(array):
    a_list = []
    for i in array:
        a_list.append(i ** 2 + 1)
    return a_list


@functools.lru_cache
def fibonacci_fast(n):
    if n <= 1:
        return 1
    else:
        return fibonacci_fast(n - 1) + fibonacci_fast(n - 2)


def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 1000

    # print("Fibonacci slow")
    # start = time.time()
    # print(fibonacci(n))
    # print(time.time() -start)


    print("Squares not-optimized")
    start = time.time()
    find_squares(range(n))
    # print(find_squares(range(n)))
    t1 = time.time() - start
    print(t1)
    print("Squares optimized")
    start = time.time()
    find_squares_opt(range(n))
    # print(find_squares_opt(range(n)))
    t2 = time.time() - start
    print(t2)
    print(t1/t2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
