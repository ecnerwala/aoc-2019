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

    out_deg = defaultdict(lambda:0)
    formulas = {}
    for l in inp:
        a = l.split()
        assert a[-3] == '=>'
        a = a[:-3] + a[-2:]
        formulas[a[-1]] = [(int(x), y.rstrip(',')) for x,y in zip(a[0::2], a[1::2])]
        out_deg[a[-1]] += 0
        for _, y in formulas[a[-1]][:-1]:
            out_deg[y] += 1
    need = defaultdict(lambda:0)
    need['FUEL'] = 1
    queue = [a for a, v in out_deg.items() if v == 0]
    #assert 'FUEL' in queue
    for z in queue:
        if z == 'ORE':break
        cnt = formulas[z][-1][0]
        mult = (need[z] + cnt - 1) // cnt
        for v, t in formulas[z][:-1]:
            need[t] += mult * v
            out_deg[t] -= 1
            if out_deg[t] == 0:
                queue.append(t)
    cprint(need['ORE'])

    @lru_cache(maxsize=None)
    def get_ways(out):
        # How much ore is required for the smallest amt, what is the smallest amt
        if out == 'ORE': return 1, 1
        tot_ore = 0
        mult = 1
        for v, t in formulas[out][:-1]:
            # We need mult * v = cur_num * something
            cur_ore, cur_num = get_ways(t)

            g = cur_num // gcd(v, cur_num)
            tot_ore *= g
            mult *= g

            assert mult * v % cur_num == 0

            k = mult * v // cur_num
            cur_ore *= k
            cur_num *= k

            tot_ore += cur_ore

        mult *= formulas[out][-1][0]
        return tot_ore, mult

    x, y = get_ways('FUEL')
    print(x,y)
    cprint(1000000000000 * y / x)




samp_inp = r"""
157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT
"""

real_inp = r"""
165 ORE => 2 PNBGW
2 FTZDF, 14 RHWGQ => 8 JTRM
1 QSKQ, 1 GPRK => 8 HKXF
2 GKLGP => 3 MTJLK
4 HXMPQ => 8 VCRLF
2 DMXC, 2 MTJLK => 8 QSKQ
39 TCLZ, 17 DKHX, 7 HVPQT, 1 DWMW, 33 THWX, 67 JVGP, 44 RDZSG, 7 JCKT, 22 TDSC, 1 QHVR => 1 FUEL
6 VCRLF, 1 HXMPQ, 6 WQSDR => 3 GKLGP
1 WLSQZ => 1 WQSDR
1 MTJLK => 2 PVSV
5 HVPQT, 4 WCTW => 8 NWGDN
3 KNTQG => 9 TCLZ
1 JTRM, 3 QSKQ, 2 RGWB => 9 RDZSG
1 MTJLK, 15 DZMQ => 6 RCPN
1 PVSV, 3 HBWDW => 7 DZMQ
1 CTKPZ, 2 HKXF => 3 RFCDH
5 QNXTS, 2 GSJNV, 1 JVGP, 10 HJTHM, 5 HKXF, 10 DZMQ => 4 JCKT
1 PNBGW => 2 HVPQT
187 ORE => 1 XLNC
16 GPRK => 6 QNXTS
1 FTZDF => 9 GPRK
9 KNTQG => 2 WCTW
35 WQSDR, 2 HVPQT => 8 RPVGN
5 RPVGN => 2 RHWGQ
1 CTKPZ, 9 QSKQ, 2 QNXTS => 5 DTFRT
1 HXMPQ, 12 VCRLF, 1 RHQH => 6 FTZDF
3 RHWGQ, 19 DZMQ, 8 FPNMC => 9 FGNK
7 RHQH, 3 HWSG => 9 HBWDW
11 QNXTS, 1 CNVKX => 8 QHVR
4 HVPQT => 6 NRLP
4 NWGDN, 1 HWSG => 2 DMXC
20 DTFRT, 4 NRLP, 1 CTKPZ => 8 HJTHM
2 BSVPD, 7 RHQH => 6 FPNMC
3 NSRB => 4 BSVPD
1 DZMQ => 3 GSJNV
2 GMNXP, 4 GSJNV, 1 ZRBR => 3 WPWM
6 RCPN => 4 CNVKX
1 NSRB => 5 RGWB
22 VCRLF => 4 NSRB
4 XLNC, 24 KNTQG => 9 WLSQZ
36 NWGDN => 2 WQZQ
5 CPMCX, 2 FGNK, 5 DTFRT => 2 ZRBR
1 CTKPZ, 1 GMNXP, 6 QNXTS => 4 KRDWH
9 RHWGQ, 16 FTZDF, 1 JVGP, 1 GMNXP, 3 HKXF, 9 DTFRT, 27 CTKPZ, 1 GKLGP => 9 DWMW
5 WQSDR, 4 NRLP, 3 TCLZ => 1 RHQH
4 NRLP => 5 GMNXP
158 ORE => 5 KNTQG
24 GMNXP, 6 JVGP, 1 BHVR, 4 KRDWH, 1 WPWM, 2 RFCDH => 7 TDSC
1 WCTW => 7 HXMPQ
10 BSVPD => 9 THWX
18 RGWB, 1 HJTHM => 3 DKHX
1 WQZQ, 4 VCRLF, 10 HVPQT => 3 CPMCX
14 BSVPD, 6 FPNMC, 5 TCLZ => 8 JVGP
4 WQZQ, 1 HXMPQ, 4 VCRLF => 3 HWSG
2 HWSG => 9 CTKPZ
4 NSRB, 1 GPRK => 4 BHVR

"""

print("Sample:")
main(samp_inp, False)

print("Actual:")
main(real_inp, True)
