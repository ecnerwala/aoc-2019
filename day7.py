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

class NeedInput_():
    pass

NeedInput = NeedInput_()

class Computer():
    def __init__(self, prog):
        self.mem = list(prog)
        self.pc = 0
        self.out = []


    def run_with_inp(self, inp):
        inp = iter(inp)
        while True:
            instr = self.mem[self.pc]
            op = instr % 100
            instr //= 100

            next_pc = self.pc+1

            def get_param():
                nonlocal next_pc
                nonlocal instr
                v = self.mem[next_pc]
                next_pc += 1
                mode = instr % 10
                instr //= 10
                return (mode, v)
            def get_read_param():
                mode, v = get_param()
                if mode == 0:
                    return self.mem[v]
                elif mode == 1:
                    return v
                else: assert False
            def get_write_addr():
                mode, v = get_param()
                if mode == 0:
                    return v
                elif mode == 1:
                    assert False
                else: assert False

            def do_jump(loc):
                self.pc = loc

            if op == 99:
                return None
            elif op == 1:
                s1 = get_read_param()
                s2 = get_read_param()
                d = get_write_addr()
                self.mem[d] = s1 + s2
            elif op == 2:
                s1 = get_read_param()
                s2 = get_read_param()
                d = get_write_addr()
                self.mem[d] = s1 * s2
            elif op == 3:
                try:
                    v = next(inp)
                except StopIteration:
                    return NeedInput
                d = get_write_addr()
                self.mem[d] = v
            elif op == 4:
                s = get_read_param()
                self.out.append(s)
            elif op == 5:
                s1 = get_read_param()
                s2 = get_read_param()
                if s1 != 0:
                    next_pc = s2
            elif op == 6:
                s1 = get_read_param()
                s2 = get_read_param()
                if s1 == 0:
                    next_pc = s2
            elif op == 7:
                s1 = get_read_param()
                s2 = get_read_param()
                d = get_write_addr()
                self.mem[d] = (1 if s1 < s2 else 0)
            elif op == 8:
                s1 = get_read_param()
                s2 = get_read_param()
                d = get_write_addr()
                self.mem[d] = (1 if s1 == s2 else 0)
            else: assert False

            self.pc = next_pc


def main(inp, is_real):
    if not is_real: return

    inp = inp.strip()
    inp = inp.split(',')

    prog = tuple(map(int, inp))

    ans = -1
    def try_perm(perm):
        amps = [Computer(prog) for _ in range(5)]
        for i in range(5):
            amps[i].run_with_inp([perm[i]])

        v = 0
        while True:
            for i in range(5):
                loc = len(amps[i].out)
                resp = amps[i].run_with_inp([v])
                if len(amps[i].out) == loc:
                    assert resp is None
                    assert i == 0
                    return v
                assert len(amps[i].out) == loc+1
                v = amps[i].out[loc]

    cprint(max(try_perm(perm) for perm in permutations(range(5,10))))

    #exit(0)



samp_inp = r"""
"""

real_inp = r"""
3,8,1001,8,10,8,105,1,0,0,21,30,39,64,81,102,183,264,345,426,99999,3,9,1001,9,2,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,1002,9,5,9,101,2,9,9,102,3,9,9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99
"""

print("Sample:")
main(samp_inp, False)

print("Actual:")
main(real_inp, True)
