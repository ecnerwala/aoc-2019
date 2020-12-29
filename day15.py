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

    panels = defaultdict(lambda: 0)
    comp = Computer(prog)

    wall = {}
    tgt = None

    def print_wall():
        grid = ''
        for y in range(max(y for x,y in wall), min(y for x,y in wall)-1,-1):
            for x in range(min(x for x,y in wall), max(x for x,y in wall)+1):
                if (x,y) not in wall: grid += ' '
                elif wall[x,y]: grid += '#'
                else: grid += '.'
            grid += '\n'
    def dfs(p):
        nonlocal tgt
        assert p in wall
        assert not wall[p]
        print_wall()
        for cmd, (dx, dy) in [(1, (0,1)), (2, (0,-1)), (3, (-1,0)), (4, (1,0))]:
            np = (p[0]+dx, p[1]+dy)
            if np in wall: continue
            comp.run_with_inp([cmd])
            resp = comp.pop_output()
            if resp == 0:
                wall[np] = True
                continue
            else:
                if resp == 2:
                    assert tgt is None
                    tgt = np
                wall[np] = False
                dfs(np)
                comp.run_with_inp([[0,2,1,4,3][cmd]])
                resp = comp.pop_output()
                assert resp != 0

    wall[(0,0)] = False
    dfs((0,0))
    vis = defaultdict(lambda:False)
    dist = {}
    q = [tgt]
    dist[tgt] = 0
    for x,y in q:
        assert not wall[x,y]
        for cmd, (dx, dy) in [(1, (0,1)), (2, (0,-1)), (3, (-1,0)), (4, (1,0))]:
            nx,ny = x+dx,y+dy
            if not wall[nx,ny] and (nx,ny) not in dist:
                dist[nx,ny] = dist[x,y]+1
                q.append((nx,ny))
    cprint(max(dist.values()))

    #exit(0)



samp_inp = r"""
"""

real_inp = r"""
3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,101,0,1034,1039,1001,1036,0,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1105,1,124,102,1,1034,1039,1002,1036,1,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1106,0,124,1001,1034,-1,1039,1008,1036,0,1041,1002,1035,1,1040,102,1,1038,1043,102,1,1037,1042,1106,0,124,1001,1034,1,1039,1008,1036,0,1041,1001,1035,0,1040,1002,1038,1,1043,101,0,1037,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,37,1032,1006,1032,165,1008,1040,33,1032,1006,1032,165,1101,0,2,1044,1106,0,224,2,1041,1043,1032,1006,1032,179,1101,0,1,1044,1105,1,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,62,1044,1106,0,224,1101,0,0,1044,1106,0,224,1006,1044,247,101,0,1039,1034,1002,1040,1,1035,102,1,1041,1036,101,0,1043,1038,1001,1042,0,1037,4,1044,1106,0,0,60,10,88,42,71,78,10,10,70,23,65,29,47,58,86,53,77,61,77,63,18,9,20,68,45,15,67,3,95,10,14,30,81,53,3,83,46,31,95,43,94,40,21,54,93,91,35,80,9,17,81,94,59,83,49,96,61,63,24,85,69,82,45,71,48,39,32,69,93,11,90,19,78,54,79,66,6,13,76,2,67,69,10,9,66,43,73,2,92,39,12,99,33,89,18,9,78,11,96,23,55,96,49,12,85,93,49,22,70,93,59,76,68,55,66,54,32,34,36,53,64,84,87,61,43,79,7,9,66,40,69,9,76,92,18,78,49,39,80,32,70,52,74,37,86,11,77,51,15,28,84,19,13,75,28,86,3,82,93,15,79,61,93,93,31,87,43,67,44,83,78,43,46,46,12,89,19,85,44,95,65,24,70,93,50,98,72,66,80,23,87,19,97,40,25,9,49,6,81,35,9,52,71,27,63,3,96,94,21,24,48,79,67,72,72,15,85,93,22,95,34,3,63,21,79,9,51,92,45,87,25,41,80,13,88,68,66,18,85,75,39,80,17,54,93,89,65,21,91,73,53,60,69,29,82,99,5,22,65,9,69,61,80,63,38,71,61,61,11,68,30,74,11,26,53,59,97,2,12,74,79,44,73,72,27,17,34,92,26,27,88,66,5,97,34,81,86,30,35,6,64,36,34,65,80,12,90,65,95,21,90,55,43,71,89,56,97,91,27,27,73,80,34,22,48,89,84,35,88,90,47,4,32,77,31,2,82,66,76,43,74,68,56,78,36,59,66,58,75,89,96,51,51,97,34,49,86,70,26,46,89,43,99,97,66,32,51,32,77,33,86,92,56,68,64,39,83,55,25,98,24,56,73,21,98,39,24,67,21,4,76,10,32,91,53,82,37,59,72,63,78,43,67,2,72,69,50,71,19,72,92,51,12,93,61,88,24,84,35,93,30,63,70,7,78,83,42,63,6,25,24,73,76,22,99,68,14,85,14,75,32,88,42,47,97,2,91,97,51,79,12,71,91,7,1,87,82,21,98,63,37,19,85,1,48,77,54,76,12,92,28,91,25,85,88,8,92,32,67,18,56,51,67,58,80,59,77,76,25,7,73,58,72,96,75,15,27,37,23,83,58,68,83,50,67,41,39,89,24,1,83,63,8,64,54,76,50,3,89,97,74,48,15,91,22,37,71,77,9,1,85,38,23,58,10,75,86,72,80,59,24,64,7,63,85,53,61,89,68,7,80,4,68,56,39,66,31,69,6,7,76,88,17,89,42,64,56,11,97,65,64,71,88,61,31,32,53,88,99,55,73,20,90,10,86,32,50,89,53,83,42,80,28,63,98,38,85,72,57,88,23,52,96,77,39,65,88,40,26,91,56,1,94,51,94,24,20,81,74,23,45,72,56,22,84,70,44,50,68,32,98,51,75,3,61,75,59,3,7,98,76,45,78,47,74,60,69,78,54,67,29,63,47,79,72,57,73,44,63,98,6,93,36,20,27,90,77,39,44,64,68,47,48,69,78,29,76,48,1,81,10,67,32,72,47,89,83,18,39,85,65,97,15,59,13,74,29,84,50,80,94,8,27,83,67,43,75,52,96,17,82,29,83,45,85,82,71,76,44,30,10,91,16,7,31,63,2,68,75,46,70,28,93,91,17,13,81,57,93,32,27,65,61,93,11,84,10,66,14,83,14,77,26,77,13,86,21,84,87,87,34,99,69,88,1,74,61,72,54,93,16,76,54,86,63,94,13,79,24,97,0,0,21,21,1,10,1,0,0,0,0,0,0
"""

print("Sample:")
main(samp_inp, False)

print("Actual:")
main(real_inp, True)
