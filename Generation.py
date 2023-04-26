from random import randint
import time
import numpy
from numpy import log as ln
from numpy import fabs as modul
from numpy import int_
import random


def method_smirnov_transform(size):
    """
    Метод преобразований Смирнова [0, 10000]
    """
    lambd = 0.05
    stage1 = numpy.random.random_integers(1, 10000, size)  # random.sample(range(1, 10000), size)
    return [int(int_(modul(ln(1-u)/(-lambd)))) for u in stage1]


def method_middle_products(size):
    """
    Метод серединных произведений [0, 10000]
    """
    r0 = int(time.time()) % 128 + 1
    r1 = int(time.time()) % 128 + 1
    b = 11
    res = []

    for i in range(size):
        r = (r0 * r1 * b) & 10000
        res.append(r)
        r0 = r1
        r1 = r
        r0 += 12
        r1 += 16
        b += 2
    return res

