#!/usr/bin/env python2
# -*- coding: utf-8 -*-

""" 

:mod:`lab11_generators` --- Generators
======================================

Write a generator that returns an increasing integer (if the integer is even) or the string "odd" if the integer is odd.

Test your generator by calling next() 4 times.

"""

if __name__ == "__main__":
    #to use call gen.next()
    gen = (x ** 2 for x in (1, 2, 3))

    def fn(n):
        x = n
        while True:
            yield x ** 2
            x += 1

    # actual lab function
    def generator(x):
        while True:
            if x % 2 == 0:
                yield x
            else:
                yield "odd"
            x += 1


