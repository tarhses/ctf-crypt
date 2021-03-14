# CTF Crypt

## Cyber Security Challenge Belgium 2021

### What's here?

* [`lsb.py`](beep/lsb.py) &mdash; Transform an image to highlight its least significant bits.

  * Usage: `./lsb.py input output`
  * Dependencies: [Pillow](https://pillow.readthedocs.io/en/stable/)

* [`flip.py`](get-flipped/flip.py) &mdash; Flip every bit of data.

  * Usage: `cat file | ./flip.py > out`

* [`wav2bin.py`](strange-sounds/wav2bin.py) &mdash; Interpret wav data as a binary signal.

  * Usage: `cat file.wav | ./wav2bin.py 0.4 > bin.txt`

    where `0.4` is the duration of a bit (in seconds).

* [`bin2morse.py`](strange-sounds/bin2morse.py) &mdash; Interpret a binary signal as morse.

  * Usage: `cat bin.txt | ./bin2morse.py > morse.txt`