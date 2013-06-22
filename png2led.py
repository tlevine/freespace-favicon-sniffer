#!/usr/bin/env python2
from PIL import Image

def _grid_column(x):
    'param x: column, indexed at zero'
    start = x * 25
    numbers = range(start, start + 25)
    if x % 2 == 0:
        return numbers
    else:
        return list(reversed(numbers))

def grid():
    out = []
    for x in range(25):
        out.extend([(x,y) for y in _grid_column(x)])
    return out

# im = Image.open('led.png')
