import ezthread as ez
from time import sleep
from random import random


def test(number):
    sleep(random())
    return number


def callback1(rng, number):
    print("1. {} Finished ({:.2f})".format(number, rng))


def callback2(rng, number):
    print("2. {} Finished ({:.2f})".format(number, rng))


if __name__ == '__main__':
    pool = ez.pool()

    for i in range(10):
        future = pool.submit(test, i)
        future.callback(callback1, random())
        future.callback(callback2, random())

    pool.await()
