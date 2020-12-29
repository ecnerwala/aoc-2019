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
    inp = inp.strip()
    inp = inp.split('\n')

    grid = frozenset((i,j,0) for i,r in enumerate(inp) for j,v in enumerate(r) if v == '#')
    def f(g):
        cnt = Counter(v for x,y,z in g for a in [(x-1,y), (x,y-1),(x+1,y),(x,y+1)]
            for v in (
                [(i,j,z+1) for i in range(5) for j in range(5) if (2+(i+x-a[0])//5, 2+(j+y-a[1])//5) == (x,y)]
                if a == (2,2) else
                (
                    [(a[0],a[1],z)]
                    if 0 <= a[0] < 5 and 0 <= a[1] < 5 else
                    [(2 + a[0]//5, 2 + a[1]//5, z-1)]
                )
            ))
        return frozenset(p for p, c in cnt.items() if c == 1 or (c == 2 and p not in g))


    for _ in range(200):
        grid = f(grid)
    #print(grid)
    cprint(len(grid))

    #exit(0)



samp_inp = r"""
....#
#..#.
#..##
..#..
#....
"""

real_inp = r"""
###.#
..#..
#..#.
#....
.#.#.
"""

print("Sample:")
main(samp_inp, False)

print("Actual:")
main(real_inp, True)
