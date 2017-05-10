#!/usr/bin/env python3

from PIL import Image
import sys

def lsb(filename, s):
    img = Image.open(filename)

    w, h = img.size
    if len(s) * 8 > w * h:
        print("error: string is too long")
        sys.exit(1)
    
    bits = []
    for c in s:
        binary = '{:08b}'.format(ord(c))
        for bit in binary:
            bits.append(int(bit))

    i = 0
    for y in range(h):
        for x in range(w):
            r, g, b, a = img.getpixel((x, y))
            if i < len(bits):
                r = r & ~1 | bits[i]
                i += 1
            else:
                r = r & ~1
            img.putpixel((x, y), (r, g, b, a))

    img.save("out.png")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage: ./lsb.py <filename> <string>")
        sys.exit(1)

    lsb(sys.argv[1], sys.argv[2])
