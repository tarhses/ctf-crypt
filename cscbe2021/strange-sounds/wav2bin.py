#!/usr/bin/env python3

import wave
from sys import argv, stdin, stdout


def main(sample_duration: str):
    buffer = bytearray()
    with wave.open(stdin.buffer) as audio:
        sample_size = int(float(sample_duration) * audio.getframerate())
        while sample := audio.readframes(sample_size):
            normalized = [abs(frame - 128) for frame in sample]
            average = sum(normalized) / len(normalized)
            buffer.append(ord('0') if average < 30 else ord('1'))

    stdout.buffer.write(buffer)


if __name__ == '__main__':
    main(*argv[1:])
