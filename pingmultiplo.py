import os
import time

with open('ip.txt') as file:
    dump = file.read()
    dump1 = dump.splitlines()

    for line in dump1:
        os.system(f'ping -c 4 {line}')
        time.sleep(5)

    print(dump1)
