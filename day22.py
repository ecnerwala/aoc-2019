from functools import *
from collections import *
from itertools import *
from math import *
from sys import exit
from dataclasses import dataclass
import re
from builtins import pow
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
import pyperclip


def cprint(a):
    print(a)
    pyperclip.copy(a)


def main(inp, is_real):
    if not is_real: return
    inp = inp.strip()
    inp = inp.split('\n')

    MOD = 119315717514047

    a, b = 1, 0
    for l in inp:
        x, v = l.split()
        v = int(v)
        if x == 'cut':
            b -= v
            b %= MOD
        elif x == 'incr':
            a *= v
            a %= MOD
            b *= v
            b %= MOD
        elif x == 'reverse':
            b = -1 - b
            b %= MOD
            a = -a
            a %= MOD

    def comp(x, y):
        return ((x[0] * y[0]) % MOD, (x[0] * y[1] + x[1]) % MOD)

    def exp(a, b):
        st = (1, 0)
        while b:
            if b & 1: st = comp(st, a)
            a = comp(a, a)
            b >>= 1
        return st

    a, b = exp((a,b), 101741582076661)
    # ai + b = 2020 mod MOD
    def minv(a, m):
        return 1 if a == 1 else m - minv(m%a, a) * m // a
    cprint((2020 - b) * minv(a, MOD) % MOD)

    #print((a*2019+b) % MOD)


    #exit(0)



samp_inp = r"""

"""

real_inp = r"""
cut 578
incr 25
cut -3085
incr 16
cut -6620
incr 17
cut -1305
incr 71
cut -4578
incr 44
cut 5639
incr 74
reverse 0
incr 39
cut 7888
incr 17
reverse 0
cut 6512
incr 46
cut -8989
incr 46
cut -8518
incr 75
cut -870
reverse 0
incr 53
cut 7377
incr 60
cut -4733
incr 25
cut -6914
incr 23
cut -4379
reverse 0
cut 582
incr 35
cut 9853
incr 2
cut -142
incr 74
cut 328
reverse 0
incr 75
reverse 0
cut -8439
reverse 0
incr 34
cut 2121
incr 2
cut 8335
incr 65
cut -1254
reverse 0
cut -122
incr 75
cut -9227
reverse 0
incr 24
cut 3976
reverse 0
incr 8
cut -3292
incr 4
reverse 0
cut -8851
incr 2
reverse 0
cut 4333
incr 73
reverse 0
incr 9
cut -7880
incr 49
cut 9770
incr 30
cut 2701
incr 59
cut 4292
incr 37
reverse 0
cut -184
incr 25
cut 9907
incr 46
reverse 0
cut 902
incr 46
cut 2622
reverse 0
cut 637
incr 58
cut 7354
incr 69
reverse 0
incr 49
reverse 0
incr 19
cut -8342
incr 68
reverse 0
"""

print("Sample:")
main(samp_inp, False)

print("Actual:")
main(real_inp, True)
