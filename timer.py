#!/usr/bin/env python3

import sys
import time
import blessed

seconds = int(sys.argv[1])
term = blessed.Terminal()

for s in range(seconds, 0, -1):
    sys.stdout.write(str(s))
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write(term.clear_bol + term.move_x(0))

sys.stdout.write("0\n")
