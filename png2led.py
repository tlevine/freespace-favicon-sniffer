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
    grid_dict = {}
    for x in range(25):
        col = _grid_column(x)
        for y in range(25):
            grid_dict[col[y]] = (x,y)
    return [grid_dict[i] for i in sorted(grid_dict.keys())]

def frame(filename):
    im = Image.open(filename)
    frame = '\x00\x00\x07\x53'
    for i, xy  in enumerate(grid()):
        r,g,b = im.getpixel(xy)
        frame +=

