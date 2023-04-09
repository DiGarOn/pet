# есть функция сложения 2х чисел. надо написать декоратор, который выводит время работы описанной ранее функции

import time


def sum_decor(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep()
        res = func(*args, **kwargs)
        end = time.time()
        return end-start, res
    return wrapper


@sum_decor
def sum_t(a, b):
    return a+b

print(sum_t(1,2))