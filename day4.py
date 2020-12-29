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
    a, b = map(int, inp.split('-'))

    def is_good(v):
        v = str(v)
        return sorted(v) == list(v) and 2 in set(Counter(v).values())

    cprint(sum(is_good(x) for x in range(a, b+1)))

    #exit(0)



samp_inp = r"""

"""

real_inp = r"""
234208-765869
"""

print("Sample:")
main(samp_inp, False)

print("Actual:")
main(real_inp, True)
