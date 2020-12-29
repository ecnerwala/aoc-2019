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


def main(inp, is_real):
    if not is_real: return

    inp = inp.strip()
    inp = inp.split(',')

    prog = tuple(map(int, inp))

    panels = defaultdict(lambda: 0)
    comp = Computer(prog).run_with_inp()


    x,y = 0,0
    dx, dy = 0,1

    panels[(x,y)] = 1

    while not comp.run_with_inp().halted:
        comp.run_with_inp([panels[(x,y)]])
        panels[x,y] = comp.pop_output()
        d = comp.pop_output()
        if d == 0:
            # Turn left
            dx, dy = -dy, dx
        elif d == 1:
            dx, dy = dy, -dx
        else: assert False, d
        x += dx
        y += dy

    x0 = min(x for x,y in panels)
    x1 = max(x for x,y in panels)+1
    y0 = min(y for x,y in panels)
    y1 = max(y for x,y in panels)+1
    for y in range(y1-1,y0-1,-1):
        print(''.join(' X'[panels[x,y]] for x in range(x0,x1)))

    #exit(0)



samp_inp = r"""
"""

real_inp = r"""
3,8,1005,8,318,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,29,1006,0,99,1006,0,81,1006,0,29,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,59,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,82,1,1103,3,10,2,104,14,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,111,1,108,2,10,2,1101,7,10,1,1,8,10,1,1009,5,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,149,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,172,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,193,1006,0,39,2,103,4,10,2,1103,20,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,227,1,1106,8,10,2,109,15,10,2,106,14,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,261,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,283,1,1109,9,10,2,1109,5,10,2,1,2,10,1006,0,79,101,1,9,9,1007,9,1087,10,1005,10,15,99,109,640,104,0,104,1,21101,936333124392,0,1,21101,0,335,0,1106,0,439,21102,1,824663880596,1,21102,346,1,0,1105,1,439,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,1,179519553539,1,21101,393,0,0,1106,0,439,21102,46266515623,1,1,21101,0,404,0,1106,0,439,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,983925826324,1,21101,0,427,0,1106,0,439,21101,988220642048,0,1,21102,1,438,0,1105,1,439,99,109,2,21201,-1,0,1,21102,1,40,2,21101,0,470,3,21101,460,0,0,1106,0,503,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,465,466,481,4,0,1001,465,1,465,108,4,465,10,1006,10,497,1101,0,0,465,109,-2,2106,0,0,0,109,4,2102,1,-1,502,1207,-3,0,10,1006,10,520,21101,0,0,-3,22102,1,-3,1,21202,-2,1,2,21102,1,1,3,21102,1,539,0,1105,1,544,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,567,2207,-4,-2,10,1006,10,567,21202,-4,1,-4,1106,0,635,21202,-4,1,1,21201,-3,-1,2,21202,-2,2,3,21102,1,586,0,1105,1,544,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,605,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,627,21202,-1,1,1,21102,1,627,0,105,1,502,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0
"""

print("Sample:")
main(samp_inp, False)

print("Actual:")
main(real_inp, True)
