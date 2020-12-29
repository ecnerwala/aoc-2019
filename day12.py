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

def signum(a): return (a > 0) - (a < 0)


def main(inp, is_real):
    inp = inp.strip()
    inp = list(map(eval, inp.split('\n')))

    def solve_dim(inp):
        print(inp)
        moons = [[a, 0] for a in inp]
        cur_time = 0
        seen = {}
        while True:
            state = tuple(z for x in moons for z in x)
            if state in seen:
                print(cur_time - seen[state])
                return cur_time - seen[state]
            seen[state] = cur_time

            for i in range(len(moons)):
                for j in range(len(moons)):
                    if i == j: continue
                    moons[i][1] += signum(moons[j][0] - moons[i][0])
            for i in range(len(moons)):
                moons[i][0] += moons[i][1]
            cur_time += 1

    resps = [*map(solve_dim, zip(*inp))]
    ans = 1
    for v in resps: ans *= v // gcd(v, ans)
    print(ans)

    #exit(0)



samp_inp = r"""
(-1, 0, 2)
(2, -10, -7)
(4, -8, 8)
(3, 5, -1)
"""

real_inp = r"""
(8, 0, 8)
(0, -5, -10)
(16, 10, -5)
(19, -10, -7)
"""

print("Sample:")
main(samp_inp, False)

print("Actual:")
main(real_inp, True)
