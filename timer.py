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
        echo(f"\n  {s}\n\n")
        time.sleep(1)
        echo(term.move_up(3) + term.move_x(0) + term.clear_eos())

echo("\n  0\n\n")
