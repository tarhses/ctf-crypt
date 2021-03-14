#!/usr/bin/env python3

from sys import stdin, stdout


def main():
    stdout.buffer.write(stdin.buffer.read()
        .replace(b'000', b'/')
        .replace(b'111', b'_')
        .replace(b'0', b'')
        .replace(b'1', b'.'))


if __name__ == '__main__':
    main()
