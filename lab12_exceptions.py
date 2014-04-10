#!/usr/bin/env python2 # -*- coding: utf-8 -*-

""" 

:mod:`lab12_exceptions` --- Exceptions
======================================

 Open a non-existent file with open() and catch the resulting exception.

 In the interrupt handler for the IOError, print "IOError: Damn the Torpedoes!" then go into an infinite loop sleeping 1 second at a time.  You must get out with Ctrl-C. Catch the Ctrl-C and in the finally clause print "Carry On!"

"""

if __name__ == "__main__":
    try:
        open('foo.', 'r')
    except IOError:
        print "IOError: Damn the Torpedoes!"
        while True:
            import time
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                import sys
                sys.exit(0)
    finally:
        print "\nCarry On!"
