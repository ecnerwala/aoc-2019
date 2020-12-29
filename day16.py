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
    inp = list(map(int, inp))
    inp = inp * 10000
    print(len(inp))

    pref = [0] * (len(inp)+1)

    for _ in range(100 if is_real else 4):
        for i in range(len(inp))
        ninp = [
            int(str(sum(v * [0,1,0,-1][(j+1)//(i+1)%4] for j, v in enumerate(inp)))[-1])
            for i in range(len(inp))
        ]
        inp = ninp
    cprint(''.join(map(str, inp[:8])))

    #exit(0)



samp_inp = r"""
12345678
"""

real_inp = r"""
59773419794631560412886746550049210714854107066028081032096591759575145680294995770741204955183395640103527371801225795364363411455113236683168088750631442993123053909358252440339859092431844641600092736006758954422097244486920945182483159023820538645717611051770509314159895220529097322723261391627686997403783043710213655074108451646685558064317469095295303320622883691266307865809481566214524686422834824930414730886697237161697731339757655485312568793531202988525963494119232351266908405705634244498096660057021101738706453735025060225814133166491989584616948876879383198021336484629381888934600383957019607807995278899293254143523702000576897358
"""

print("Sample:")
main(samp_inp, False)

print("Actual:")
main(real_inp, True)
