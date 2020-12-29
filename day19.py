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
        self.mem = defaultdict(lambda: 0)
        for i,v in enumerate(prog):
            self.mem[i] = v
        self.pc = 0
        self.out = []
        self.relative_base = 0
        self.halted = False

        self.out_ctr = 0


    def run_with_inp(self, inp=None):
        if self.halted: return self

        if inp is None: inp = []

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
                elif mode == 2:
                    addr = self.relative_base + v
                    assert 0 <= addr
                    return self.mem[addr]
                else: assert False
            def get_write_addr():
                mode, v = get_param()
                if mode == 0:
                    return v
                elif mode == 1:
                    assert False
                elif mode == 2:
                    addr = self.relative_base + v
                    assert 0 <= addr
                    return addr
                else: assert False

            def do_jump(loc):
                self.pc = loc

            if op == 99:
                self.halted = True
                return self
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
                    return self
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
            elif op == 9:
                s1 = get_read_param()
                self.relative_base += s1
            else: assert False

            self.pc = next_pc

    def pop_output(self, l=None):
        if l is None:
            return self.pop_output(1)[0]
        assert l + self.out_ctr <= len(self.out)
        self.out_ctr += l
        return self.out[self.out_ctr-l:self.out_ctr]

    def has_output(self, l=1):
        return self.out_ctr + l <= len(self.out)


def main(inp, is_real):
    if not is_real: return

    inp = inp.strip()
    inp = inp.split(',')

    prog = tuple(map(int, inp))

    def get_beam(i,j):
        if i < 0 or j < 0: return False
        return Computer(prog).run_with_inp([i,j]).pop_output() == 1

    for i in range(1000):
        if i >= 2:
            assert get_beam(i, (3*i+1)//2)
    for i in range(60):
        s = ''
        for j in range(60):
            s += '.#'[get_beam(i,j)]
        print(s)

    def get_diag_first(s):
        r = s * 2 // 5
        c = s - r
        while not get_beam(r, c):
            r -= 1
            c += 1
        while get_beam(r+1, c-1):
            r += 1
            c -= 1
        assert get_beam(r, c)
        return r,c

    def get_diag_width(s):
        r, c = get_diag_first(s)
        lo = c 
        hi = s+1
        while hi - lo > 1:
            md = (lo + hi) >> 1
            if get_beam(s-md, md):
                lo = md
            else:
                hi = md
        return hi - c

    s = 2500
    while get_diag_width(s) < 100: s += 1
    print(s)
    r, c = get_diag_first(s)
    x, y = r - 99, c
    cprint(x*10000+y)
    for i in range(100):
        for j in range(100):
            assert get_beam(x+i, y+j)
    print(get_diag_width(s))

    for i in range(-100,100):
        s = ''
        for j in range(-100,100):
            s += '.#'[get_beam(x+i,y+j)]
        print(s)
    #exit(0)


samp_inp = r"""
"""

real_inp = r"""
109,424,203,1,21102,1,11,0,1106,0,282,21101,0,18,0,1106,0,259,1202,1,1,221,203,1,21101,0,31,0,1105,1,282,21102,38,1,0,1105,1,259,20102,1,23,2,21201,1,0,3,21102,1,1,1,21101,0,57,0,1105,1,303,2101,0,1,222,20102,1,221,3,21002,221,1,2,21101,0,259,1,21101,0,80,0,1106,0,225,21102,1,152,2,21101,91,0,0,1106,0,303,1201,1,0,223,21001,222,0,4,21101,0,259,3,21102,225,1,2,21101,0,225,1,21102,1,118,0,1105,1,225,20101,0,222,3,21102,61,1,2,21101,133,0,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21102,148,1,0,1105,1,259,2101,0,1,223,21001,221,0,4,21001,222,0,3,21101,0,14,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,0,195,0,105,1,109,20207,1,223,2,20101,0,23,1,21102,-1,1,3,21102,214,1,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2101,0,-4,249,21202,-3,1,1,21202,-2,1,2,21201,-1,0,3,21102,1,250,0,1106,0,225,22101,0,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2105,1,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22102,1,-2,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21202,-2,1,3,21101,343,0,0,1106,0,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22101,0,-4,1,21101,0,384,0,1106,0,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21201,1,0,-4,109,-5,2106,0,0
"""

print("Sample:")
main(samp_inp, False)

print("Actual:")
main(real_inp, True)
