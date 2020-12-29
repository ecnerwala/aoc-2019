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
    inp = inp.split(',')

    prog = tuple(map(int, inp))

    def run_prog(a,b):
        mem = list(prog)

        mem[1] = a
        mem[2] = b

        pc = 0
        while True:
            op = mem[pc]
            if op == 99:
                break
            elif op == 1:
                a,b,c = mem[pc+1:pc+4]
                mem[c] = mem[a] + mem[b]
                pc += 4
            elif op == 2:
                a,b,c = mem[pc+1:pc+4]
                mem[c] = mem[a] * mem[b]
                pc += 4
            else: assert False
        return mem[0]

    for i in range(100):
        for j in range(100):
            if run_prog(i, j) == 19690720:
                print(i, j)
                cprint(i*100+j)
                return
    cprint(mem[0])

    #exit(0)



samp_inp = r"""
1,9,10,3,2,3,11,0,99,30,40,50
"""

real_inp = r"""
1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,1,23,13,27,2,6,27,31,1,5,31,35,2,10,35,39,1,6,39,43,1,13,43,47,2,47,6,51,1,51,5,55,1,55,6,59,2,59,10,63,1,63,6,67,2,67,10,71,1,71,9,75,2,75,10,79,1,79,5,83,2,10,83,87,1,87,6,91,2,9,91,95,1,95,5,99,1,5,99,103,1,103,10,107,1,9,107,111,1,6,111,115,1,115,5,119,1,10,119,123,2,6,123,127,2,127,6,131,1,131,2,135,1,10,135,0,99,2,0,14,0
"""

print("Sample:")
main(samp_inp, False)

print("Actual:")
main(real_inp, True)
