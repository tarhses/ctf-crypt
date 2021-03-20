# CTF Crypt

## Cyber Security Challenge Belgium 2021

### What's here?

* [`lsb.py`](beep/lsb.py) &mdash; Transform an image to highlight its least significant bits.
  * Usage: `./lsb.py input output`
  * Dependencies: [Pillow](https://pillow.readthedocs.io/en/stable/)

* [`SavePatch.py`](dont-run-me/SavePatch.py) &mdash; Ghidra script to save an executable patched binary.
  * [Original script](https://github.com/schlafwandler/ghidra_SavePatch) by schlafwandler, I just fixed runtime errors I got.

* [`flip.py`](get-flipped/flip.py) &mdash; Flip every bit of data.
  * Usage: `cat file | ./flip.py > out`

* [`wav2bin.py`](strange-sounds/wav2bin.py) &mdash; Interpret wav data as a binary signal.
  * Usage: `cat file.wav | ./wav2bin.py 0.4 > bin.txt` where `0.4` is the duration of a bit (in seconds).

* [`bin2morse.py`](strange-sounds/bin2morse.py) &mdash; Interpret a binary signal as morse.
  * Usage: `cat bin.txt | ./bin2morse.py > morse.txt`

* [`attack_brute.py`](three-blind-mice/attack_brute.py) &mdash; Attempt a multi-threaded brute force attack against a TCP connection.
  * Usage: `./attack_brute.py <addr> <port> <thread number>` 
  * You'll need a list of passwords ([rockyou.txt](https://github.com/praetorian-inc/Hob0Rules/raw/master/wordlists/rockyou.txt.gz) or similar).
  * A list of ignored responses is hard-coded in the script.