#!/usr/bin/env python3

import sys
import time
import blessed
import re
from functools import partial

echo = partial(print, end="", flush=True)
term = blessed.Terminal()

total_seconds = 0
a = re.split(":|\\.", sys.argv[1])

match len(a):
    case 1:
        total_seconds = int(a[0]) * 60
    case 2:
        total_seconds = int(a[0]) * 60 + int(a[1])
    case 3:
        total_seconds = int(a[0]) * 60*60 + int(a[1]) * 60 + int(a[2])


with term.cbreak():
    for seconds_left in range(total_seconds, 0, -1):
        h = seconds_left // 3600
        m = seconds_left % 3600 // 60
        s = seconds_left % 60

        echo("\n  ")

        if (h > 0):
            echo(f"{h}:{m:02}:{s:02}")
        else:
            echo(f"{m}:{s:02}")

        echo("\n\n")

        time.sleep(1)

        echo(term.move_up(3) + term.move_x(0) + term.clear_eos())

echo("\n  0:00\n\n")
