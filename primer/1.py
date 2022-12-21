#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def sr_geom(*args):
    if args:
        values = [float(arg) for arg in args]
        g = 1
        for arg in values:
            g *= arg
        n = len(values)
        return pow(g, 1 / n)
    else:
        return None


if __name__ == '__main__':
    print(f"Среднее геометрическое чисел= {sr_geom()}")
    print(f"Среднее геометрическое чисел= {sr_geom(1, 2, 3, 4, 5)}")
    print(f"Среднее геометрическое чисел= {sr_geom(6, 2, 7, 4)}")
