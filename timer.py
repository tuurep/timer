#!/usr/bin/env python3

import sys
import time
import blessed
from functools import partial

echo = partial(print, end="", flush=True)

seconds = int(sys.argv[1])
term = blessed.Terminal()

with term.cbreak():
    for s in range(seconds, 0, -1):
        echo(s)
        time.sleep(1)
        echo(term.clear_bol + term.move_x(0))

echo("0\n")
