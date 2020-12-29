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

    def all_output(self):
        return self.pop_output(len(self.out) - self.out_ctr)


def main(inp, is_real):
    if not is_real: return

    inp = inp.strip()
    inp = inp.split(',')

    prog = tuple(map(int, inp))
    comp = Computer(prog)
    s = [
        # (6 OR 9) AND 5 OR 8 AND 4, then can jump
        # that OR 7 AND 3 OR 6 AND 2 OR ((6 OR 9) AND 5) AND 1 => can walk
        # ans = can jump and not walk
        'OR I T',
        'OR F T',
        'AND E T',

        'NOT T J',
        'NOT J J',
        'OR G J',
        'AND C J',
        'OR F J',
        'AND B J',
        'OR T J',
        'AND A J',
        # T = 1-good; if not T, then J

        'NOT J J',

        'OR H T',
        'AND D T', # T = 4-good; if not T, then not J

        'AND T J',
        'RUN',
    ]

    # not (1 and 2 and 3) and (((6 or 9) and 5) or 8) and 4
    s = [
        # (6 OR 9) AND 5 OR 8 AND 4, then can jump
        # that OR 7 AND 3 OR 6 AND 2 OR ((6 OR 9) AND 5) AND 1 => can walk
        # ans = can jump and not walk
        'NOT A J',
        'NOT J J',
        'AND B J',
        'AND C J',
        'NOT J J',

        'NOT I T',
        'NOT T T',
        'OR F T',
        'AND E T',
        'OR H T',
        'AND D T', # T = 4-good; if not T, then not J
        'AND T J',

        'RUN',
    ]
    comp.run_with_inp(list(map(ord, ''.join(line + '\n' for line in s))))
    print(''.join(map(chr, comp.all_output()[:-1])))
    cprint(comp.out[-1])
    #exit(0)



samp_inp = r"""
"""

real_inp = r"""
109,2050,21101,966,0,1,21101,0,13,0,1106,0,1378,21101,0,20,0,1105,1,1337,21102,1,27,0,1106,0,1279,1208,1,65,748,1005,748,73,1208,1,79,748,1005,748,110,1208,1,78,748,1005,748,132,1208,1,87,748,1005,748,169,1208,1,82,748,1005,748,239,21101,1041,0,1,21101,73,0,0,1105,1,1421,21101,0,78,1,21102,1041,1,2,21102,1,88,0,1105,1,1301,21101,68,0,1,21101,0,1041,2,21101,0,103,0,1106,0,1301,1102,1,1,750,1105,1,298,21101,82,0,1,21101,0,1041,2,21101,0,125,0,1106,0,1301,1101,2,0,750,1105,1,298,21102,79,1,1,21101,1041,0,2,21102,1,147,0,1106,0,1301,21101,84,0,1,21101,1041,0,2,21101,162,0,0,1106,0,1301,1101,0,3,750,1106,0,298,21102,65,1,1,21102,1041,1,2,21102,1,184,0,1105,1,1301,21102,76,1,1,21102,1,1041,2,21102,199,1,0,1105,1,1301,21101,0,75,1,21102,1041,1,2,21102,214,1,0,1106,0,1301,21102,221,1,0,1105,1,1337,21101,0,10,1,21101,1041,0,2,21102,1,236,0,1106,0,1301,1106,0,553,21102,1,85,1,21102,1,1041,2,21101,254,0,0,1106,0,1301,21102,1,78,1,21102,1,1041,2,21101,269,0,0,1105,1,1301,21102,276,1,0,1105,1,1337,21101,10,0,1,21102,1,1041,2,21102,291,1,0,1105,1,1301,1102,1,1,755,1106,0,553,21102,1,32,1,21102,1,1041,2,21102,313,1,0,1105,1,1301,21101,0,320,0,1106,0,1337,21101,327,0,0,1106,0,1279,1202,1,1,749,21101,65,0,2,21102,1,73,3,21101,346,0,0,1106,0,1889,1206,1,367,1007,749,69,748,1005,748,360,1102,1,1,756,1001,749,-64,751,1105,1,406,1008,749,74,748,1006,748,381,1101,0,-1,751,1106,0,406,1008,749,84,748,1006,748,395,1102,1,-2,751,1105,1,406,21101,1100,0,1,21102,406,1,0,1106,0,1421,21102,1,32,1,21101,1100,0,2,21101,421,0,0,1106,0,1301,21102,428,1,0,1106,0,1337,21101,0,435,0,1106,0,1279,2102,1,1,749,1008,749,74,748,1006,748,453,1102,-1,1,752,1105,1,478,1008,749,84,748,1006,748,467,1101,-2,0,752,1105,1,478,21101,1168,0,1,21101,0,478,0,1105,1,1421,21101,485,0,0,1106,0,1337,21102,1,10,1,21101,0,1168,2,21101,500,0,0,1106,0,1301,1007,920,15,748,1005,748,518,21101,1209,0,1,21101,0,518,0,1106,0,1421,1002,920,3,529,1001,529,921,529,1001,750,0,0,1001,529,1,537,1001,751,0,0,1001,537,1,545,1001,752,0,0,1001,920,1,920,1106,0,13,1005,755,577,1006,756,570,21102,1100,1,1,21101,0,570,0,1105,1,1421,21101,987,0,1,1106,0,581,21101,1001,0,1,21102,1,588,0,1105,1,1378,1101,758,0,594,101,0,0,753,1006,753,654,20101,0,753,1,21102,610,1,0,1105,1,667,21102,1,0,1,21101,0,621,0,1105,1,1463,1205,1,647,21101,0,1015,1,21102,1,635,0,1106,0,1378,21102,1,1,1,21102,646,1,0,1106,0,1463,99,1001,594,1,594,1105,1,592,1006,755,664,1101,0,0,755,1105,1,647,4,754,99,109,2,1101,726,0,757,22101,0,-1,1,21101,9,0,2,21101,0,697,3,21102,1,692,0,1105,1,1913,109,-2,2106,0,0,109,2,102,1,757,706,1202,-1,1,0,1001,757,1,757,109,-2,2105,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,255,63,95,223,159,191,127,0,119,108,62,102,175,57,100,197,85,154,137,93,115,185,238,140,138,155,46,42,38,162,182,86,114,78,122,116,168,34,94,99,98,190,61,174,158,169,103,214,87,126,143,179,121,50,49,218,77,120,113,236,229,181,101,56,230,232,55,71,204,156,188,243,198,117,70,79,215,184,54,59,92,166,110,109,234,202,171,216,226,35,235,142,178,186,219,107,241,167,249,170,153,251,68,123,157,111,39,231,252,84,212,163,183,124,118,227,254,242,247,253,207,106,239,189,196,233,58,152,53,43,222,203,51,244,141,220,187,125,76,201,199,228,245,139,205,173,248,213,69,246,237,221,136,250,200,177,217,47,206,60,172,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,73,110,112,117,116,32,105,110,115,116,114,117,99,116,105,111,110,115,58,10,13,10,87,97,108,107,105,110,103,46,46,46,10,10,13,10,82,117,110,110,105,110,103,46,46,46,10,10,25,10,68,105,100,110,39,116,32,109,97,107,101,32,105,116,32,97,99,114,111,115,115,58,10,10,58,73,110,118,97,108,105,100,32,111,112,101,114,97,116,105,111,110,59,32,101,120,112,101,99,116,101,100,32,115,111,109,101,116,104,105,110,103,32,108,105,107,101,32,65,78,68,44,32,79,82,44,32,111,114,32,78,79,84,67,73,110,118,97,108,105,100,32,102,105,114,115,116,32,97,114,103,117,109,101,110,116,59,32,101,120,112,101,99,116,101,100,32,115,111,109,101,116,104,105,110,103,32,108,105,107,101,32,65,44,32,66,44,32,67,44,32,68,44,32,74,44,32,111,114,32,84,40,73,110,118,97,108,105,100,32,115,101,99,111,110,100,32,97,114,103,117,109,101,110,116,59,32,101,120,112,101,99,116,101,100,32,74,32,111,114,32,84,52,79,117,116,32,111,102,32,109,101,109,111,114,121,59,32,97,116,32,109,111,115,116,32,49,53,32,105,110,115,116,114,117,99,116,105,111,110,115,32,99,97,110,32,98,101,32,115,116,111,114,101,100,0,109,1,1005,1262,1270,3,1262,21002,1262,1,0,109,-1,2105,1,0,109,1,21101,1288,0,0,1105,1,1263,20101,0,1262,0,1101,0,0,1262,109,-1,2106,0,0,109,5,21102,1,1310,0,1106,0,1279,22102,1,1,-2,22208,-2,-4,-1,1205,-1,1332,22101,0,-3,1,21102,1332,1,0,1105,1,1421,109,-5,2106,0,0,109,2,21101,1346,0,0,1105,1,1263,21208,1,32,-1,1205,-1,1363,21208,1,9,-1,1205,-1,1363,1105,1,1373,21101,0,1370,0,1106,0,1279,1105,1,1339,109,-2,2106,0,0,109,5,2102,1,-4,1386,20101,0,0,-2,22101,1,-4,-4,21101,0,0,-3,22208,-3,-2,-1,1205,-1,1416,2201,-4,-3,1408,4,0,21201,-3,1,-3,1106,0,1396,109,-5,2105,1,0,109,2,104,10,22101,0,-1,1,21102,1436,1,0,1106,0,1378,104,10,99,109,-2,2105,1,0,109,3,20002,594,753,-1,22202,-1,-2,-1,201,-1,754,754,109,-3,2105,1,0,109,10,21102,1,5,-5,21101,1,0,-4,21102,1,0,-3,1206,-9,1555,21102,3,1,-6,21102,1,5,-7,22208,-7,-5,-8,1206,-8,1507,22208,-6,-4,-8,1206,-8,1507,104,64,1105,1,1529,1205,-6,1527,1201,-7,716,1515,21002,0,-11,-8,21201,-8,46,-8,204,-8,1105,1,1529,104,46,21201,-7,1,-7,21207,-7,22,-8,1205,-8,1488,104,10,21201,-6,-1,-6,21207,-6,0,-8,1206,-8,1484,104,10,21207,-4,1,-8,1206,-8,1569,21102,0,1,-9,1105,1,1689,21208,-5,21,-8,1206,-8,1583,21102,1,1,-9,1106,0,1689,1201,-5,716,1588,21001,0,0,-2,21208,-4,1,-1,22202,-2,-1,-1,1205,-2,1613,22102,1,-5,1,21102,1,1613,0,1106,0,1444,1206,-1,1634,22101,0,-5,1,21102,1,1627,0,1106,0,1694,1206,1,1634,21101,2,0,-3,22107,1,-4,-8,22201,-1,-8,-8,1206,-8,1649,21201,-5,1,-5,1206,-3,1663,21201,-3,-1,-3,21201,-4,1,-4,1106,0,1667,21201,-4,-1,-4,21208,-4,0,-1,1201,-5,716,1676,22002,0,-1,-1,1206,-1,1686,21102,1,1,-4,1105,1,1477,109,-10,2105,1,0,109,11,21102,1,0,-6,21102,1,0,-8,21101,0,0,-7,20208,-6,920,-9,1205,-9,1880,21202,-6,3,-9,1201,-9,921,1724,21002,0,1,-5,1001,1724,1,1732,21002,0,1,-4,21202,-4,1,1,21102,1,1,2,21101,9,0,3,21102,1754,1,0,1106,0,1889,1206,1,1772,2201,-10,-4,1767,1001,1767,716,1767,20101,0,0,-3,1106,0,1790,21208,-4,-1,-9,1206,-9,1786,22101,0,-8,-3,1105,1,1790,21201,-7,0,-3,1001,1732,1,1795,21002,0,1,-2,21208,-2,-1,-9,1206,-9,1812,21201,-8,0,-1,1106,0,1816,21201,-7,0,-1,21208,-5,1,-9,1205,-9,1837,21208,-5,2,-9,1205,-9,1844,21208,-3,0,-1,1105,1,1855,22202,-3,-1,-1,1105,1,1855,22201,-3,-1,-1,22107,0,-1,-1,1106,0,1855,21208,-2,-1,-9,1206,-9,1869,21202,-1,1,-8,1106,0,1873,22101,0,-1,-7,21201,-6,1,-6,1105,1,1708,21202,-8,1,-10,109,-11,2106,0,0,109,7,22207,-6,-5,-3,22207,-4,-6,-2,22201,-3,-2,-1,21208,-1,0,-6,109,-7,2105,1,0,0,109,5,2101,0,-2,1912,21207,-4,0,-1,1206,-1,1930,21101,0,0,-4,22102,1,-4,1,22102,1,-3,2,21101,0,1,3,21101,1949,0,0,1106,0,1954,109,-5,2106,0,0,109,6,21207,-4,1,-1,1206,-1,1977,22207,-5,-3,-1,1206,-1,1977,21201,-5,0,-5,1106,0,2045,21202,-5,1,1,21201,-4,-1,2,21202,-3,2,3,21101,0,1996,0,1106,0,1954,22101,0,1,-5,21101,1,0,-2,22207,-5,-3,-1,1206,-1,2015,21102,1,0,-2,22202,-3,-2,-3,22107,0,-4,-1,1206,-1,2037,22102,1,-2,1,21102,2037,1,0,105,1,1912,21202,-3,-1,-3,22201,-5,-3,-5,109,-6,2105,1,0
"""

print("Sample:")
main(samp_inp, False)

print("Actual:")
main(real_inp, True)
