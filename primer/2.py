#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sr_harm(*args):
    if args:
        values = [float(arg) for arg in args]
        h = 0
        for arg in values:
            h += 1 / arg
        n = len(values)
        return n / h

    else:
        return None


if __name__ == '__main__':
    print(f'среднее гармоническое: {sr_harm()}')
    print(f'среднее гармоническое: {sr_harm(1, 2, 3, 4, 5)}')
    print(f'среднее гармоническое: {sr_harm(5.5, 8.1, 1.2, 5.9)}')
