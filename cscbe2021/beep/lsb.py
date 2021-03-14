#!/usr/bin/env python3

from sys import argv

from PIL import Image


def main(in_path: str, out_path: str):
    img = Image.open(in_path)
    w, h = img.size

    out = Image.new("RGB", img.size)

    x, y = 0, 0
    for r, g, b in img.getdata():
        r <<= 7
        g <<= 7
        b <<= 7

        out.putpixel((x, y), (r, g, b))

        x += 1
        if x >= w:
            x = 0
            y += 1

    out.save(out_path)


if __name__ == '__main__':
    main(*argv[1:])
