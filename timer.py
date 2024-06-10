#!/usr/bin/env python3

import sys
import time
import blessed
import re
from functools import partial

echo = partial(print, end="", flush=True)
term = blessed.Terminal()

def parse_input_to_seconds():
    # todo: handle missing args
    input = sys.argv[1]

    # h:mm:ss
    match = re.match("^(1?[0-9]|2[0-3])[:.]([0-5][0-9])[:.]([0-5][0-9])$", input)
    if match:
        h, m, s = match.groups()
        return int(h)*60*60 + int(m)*60 + int(s)

    # m:ss
    match = re.match("^([0-5]?[0-9])[:.]([0-5][0-9])$", input)
    if match:
        m, s = match.groups()
        return int(m)*60 + int(s)

    # m
    match = re.match("^([1-5]?[0-9])$", input)
    if match:
        m = match.group(1)
        return int(m) * 60

    # "1h30m30s", "2h", "50s" ...
    match = re.match("^(?:(1?[0-9]|2[0-3])h)?(?:([1-5]?[0-9])m)?(?:([1-5]?[0-9])s)?$", input)
    if match and any(match.groups()):
        h, m, s = match.groups()
        h = h or "0"
        m = m or "0"
        s = s or "0"
        return int(h)*60*60 + int(m)*60 + int(s)

    # upper limit 24h
    match = re.match("^(24h|24[:.]00[:.]00)$", input)
    if match:
        return 24*60*60

    # todo: handle invalid args
    return -1


total_seconds = parse_input_to_seconds()

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
