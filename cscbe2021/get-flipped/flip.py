#!/usr/bin/env python3

from sys import stdin, stdout


def main():
    buffer = bytearray()
    for byte in stdin.buffer.read():
        buffer.append(byte ^ 0xff)

    stdout.buffer.write(buffer)


if __name__ == '__main__':
    main()
