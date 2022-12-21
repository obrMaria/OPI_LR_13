#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 3. Сумму аргументов, расположенных
# между первым и последним нулевыми аргументами.

def summa(*args):
    if args:
        return sum(args[(args.index(0)):(len(args) - args[::-1].index(0))])
    else:
        return None


if __name__ == '__main__':
    print(summa())
    print(summa(1, -1, 0, 7, 5, 0, -9, 0, -4, 3, 1))
