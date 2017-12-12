import ezthread as ez
from time import sleep
from random import random


def test(number):
    sleep(random())
    print(number)


if __name__ == '__main__':
    pool = ez.pool()

    for i in range(10):
        pool.submit(test, i)

    pool.await()
