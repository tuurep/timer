#!/usr/bin/env python3

import sys
import time

seconds = int(sys.argv[1])

for s in range(seconds, 0, -1):
    print(s)
    time.sleep(1)

print("0 ✓")
