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
    inp = list(map(list, inp.split('\n')))

    asteroids = {(i,j) for i,r in enumerate(inp) for j,v in enumerate(r) if v == '#'}
    def red(x, y):
        assert x or y
        g = gcd(x, y)
        return x // g, y // g
    center = max(asteroids, key=lambda a:len({red(b[0]-a[0], b[1]-a[1]) for b in asteroids if b != a}))

    print(center)
    a = center

    dirs = defaultdict(list)
    for b in asteroids:
        if b == a: continue
        norm = (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
        dirs[red(b[0]-a[0], b[1]-a[1])].append((norm, b))
    for a in dirs:
        dirs[a].sort()

    s_dirs = sorted(dirs, key=lambda p: -atan2(p[1], p[0]))
    res = []
    while len(res) < 200:
        for i in s_dirs:
            if dirs[i]:
                res.append(dirs[i][0])
                dirs[i].pop(0)
    _, (x,y) = res[199]
    cprint(100*y+x)


    #exit(0)



samp_inp = r"""

.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
"""

real_inp = r"""

##.#..#..###.####...######
#..#####...###.###..#.###.
..#.#####....####.#.#...##
.##..#.#....##..##.#.#....
#.####...#.###..#.##.#..#.
..#..#.#######.####...#.##
#...####.#...#.#####..#.#.
.#..#.##.#....########..##
......##.####.#.##....####
.##.#....#####.####.#.####
..#.#.#.#....#....##.#....
....#######..#.##.#.##.###
###.#######.#..#########..
###.#.#..#....#..#.##..##.
#####.#..#.#..###.#.##.###
.#####.#####....#..###...#
##.#.......###.##.#.##....
...#.#.#.###.#.#..##..####
#....#####.##.###...####.#
#.##.#.######.##..#####.##
#.###.##..##.##.#.###..###
#.####..######...#...#####
#..#..########.#.#...#..##
.##..#.####....#..#..#....
.###.##..#####...###.#.#.#
.##..######...###..#####.#
"""

print("Sample:")
main(samp_inp, False)

print("Actual:")
main(real_inp, True)
