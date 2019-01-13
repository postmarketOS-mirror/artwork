#!/usr/bin/env python3

# Copyright 2019 Grant Miller
# SPDX-License-Identifier: CC-BY-SA-3.0


class AsciiArt():
    def __init__(self, width, height):
        self.canvas = [[' ' for _ in range(width)] for _ in range(height)]
        self.cursor = [0, 0]
        self.escape = False

    def line(self, *args):
        x1 = None
        y1 = None
        if len(args) == 1:
            x2, y2 = args[0]
        elif (len(args) == 2 and
                isinstance(args[0], int) and
                isinstance(args[1], int)):
            x2 = args[0]
            y2 = args[1]
        elif len(args) == 2 and len(args[0]) == len(args[1]) == 2:
            x1, y1 = args[0]
            x2, y2 = args[1]
        elif len(args) == 4:
            x1, y1, x2, y2 = args
        else:
            raise TypeError

        if x1 is None and y1 is None:
            x2 += self.cursor[0]
            y2 += self.cursor[1]
            x1, y1 = self.cursor
            self.cursor = [x2, y2]

        if (
                x1 % 1 == 0 and
                y1 % 1 == 0 and
                x2 % 1 == 0 and
                y2 % 1 == 0 and
                abs(x1-x2) == abs(y1-y2)):
            self._line_diagonal(x1, y1, x2, y2)

        elif (
                x1 % 1 == 0 and
                y1 % 1 == 0 and
                x2 % 1 == 0 and
                y2 % 1 == 0 and
                y1 == y2):
            self._line_horizontal_mid(x1, y1, x2, y2)
        else:
            raise NotImplementedError

    def _line_diagonal(self, x1, y1, x2, y2):
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        yrange = range(y1, y2)
        if y1 < y2:
            char = '\\'
            yrange = range(y1, y2)
        else:
            char = '/'
            yrange = reversed(range(y2, y1))
        for x, y in zip(range(x1, x2), yrange):
            self.canvas[y][x] = char

    def _line_horizontal_mid(self, x1, y1, x2, y2):
        if x1 > x2:
            x1, x2 = x2, x1
        for i in range(x1, x2):
            self.canvas[y1-1][i] = '_'

    def __str__(self):
        result = []
        for line in self.canvas:
            joined_line = ''.join(line)
            if self.escape:
                joined_line = joined_line.replace('\\', '\\\\')
            result.append(joined_line)
        return '\n'.join(result)
