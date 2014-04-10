#!/usr/bin/env python2
# -*- coding: utf-8 -*-

""" 

:mod:`lab10_string_formatting` --- String formatting
====================================================

Find some documentation on string formatting operations using the "%" operator

Print 6.2399 using a format specifier that keeps 3 decimal places

Print 0x31 using a decimal format specifier

Print 0b11011011 using a hexidecimal string format specifier

Demonstrate the other string formatting approach using format()

In lotto.py, define a new function **print_results()** that accepts one argument:
 
 A dictionary containing

 #. drawings: the number of drawings held: 104
 #. elapsed: the number of seconds the simulation took: 0.13
 #. max_ball_number: the number of balls for each pick: 54
 #. quick_pick: whether quick pick was chosen: False
 #. picks: the numbers picked to run simulation with: {33, 4, 18, 19, 52, 21}
 #. results: a dictionary containing {0:88, 1:13, 2:3, 3:0, 4:1, 5:0, 6:0}

Print a report that outputs the dictionary contents like this:

::

 Results for 104 drawings - 6 out of 54
 Selected numbers: 33, 4, 18, 19, 52, 21 
 Odds of matching all numbers: 1 in 18595558800

 # Matches   Count    Percentage
 =========   =====    ==========
    0         88       84.615
    1         13       12.500
    2          3        2.885
    3          0        0.000
    4          1        0.962
    5          0        0.000
    6          0        0.000

 Ran 104 simulations in 0.130 seconds
 For a twice-a-week lotto system, that would be the equivalent
 of 1.00 years worth of drawings.

"""

if __name__ == "__main__":
    print "%.3f" % 6.2399
    print "%d" % 0x31
    print "%x" % 0b11011011

    print "{0:.3f}".format(6.2399)
    print "{0:d}".format(0x31)
    print "{0:x}".format(0b11011011)
    print "\n"
    import lotto

    results = {
        "drawings": 104,
        "elapsed": 0.13,
        "max_ball_number": 54,
        "quick_pick": False,
        "picks": {33, 4, 18, 19, 52, 21},
        "results": {0: 88, 1: 13, 2: 3, 3: 0, 4: 1, 5: 0, 6: 0}
    }

    lotto.print_results(results)