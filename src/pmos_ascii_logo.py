#!/usr/bin/env python3

# Copyright 2019 Grant Miller
# SPDX-License-Identifier: CC-BY-SA-3.0

import argparse

from ascii_gfx import AsciiArt


def main():
    parser = argparse.ArgumentParser(
        description='Generate a postmarketOS logo in ASCII')
    parser.add_argument(
        '--height',
        type=int,
        default=20,
        help='height of logo, default 20')
    parser.add_argument(
        '--thickness',
        type=int,
        help='thickness of segments, default is scaled based on height')
    parser.add_argument(
        '--gap',
        type=int,
        default=1,
        help='size of gap between segments, default 1')
    parser.add_argument(
        '--escape',
        action='store_true',
        help='escape backslashes')
    args = parser.parse_args()

    draw(args.height, args.thickness, args.gap, args.escape)


def draw(h, t=None, gap=1, escape=False):
    if t is None:
        t = h//16 + 1

    art = AsciiArt(2*h, h)
    art.escape = escape

    # left
    art.cursor = [1, h]
    art.line(6*t-1, 0)
    art.line(t, -t)
    art.line(-t, -t)
    art.line(h-6*t-gap, 6*t-h+gap)
    art.line(-2*t, 0)
    art.line(-t, -t)
    art.line(3*t-h+gap, h-3*t-gap)

    # bottom
    art.cursor = [2*h, h]
    art.line(-3*t, -3*t)
    art.line(-2*t, 0)
    art.line(-t, t)
    art.line(-(2*h-12*t-2*gap), 0)
    art.line(t, t)
    art.line(-t, t)
    art.cursor[0] += 1
    art.line(2*h-6*t-2*gap-2, 0)

    # top
    art.cursor = [h, 0]
    art.line(-3*t, 3*t)
    art.line(t, t)
    art.line(2*t, 0)
    art.line(h-6*t-gap, h-6*t-gap)
    art.line(t, -t)
    art.line(2*t-1, 0)
    art.cursor[0] += 1
    art.line(-(h-3*t-gap), -(h-3*t-gap))

    print(art)


if __name__ == '__main__':
    main()
