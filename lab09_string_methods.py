#!/usr/bin/env python2
# -*- coding: utf-8 -*-

""" 

:mod:`lab09_string_methods` --- String Methods
==============================================

Create a new string test_string = "RaDish8"

Use the index() function to find "D" position and print the result

Print the result of isalnum() on test_string

Use a slicing to pull out the "ish" substring, then run isalpha() and print the result

Use a slicing to pull out the "8" and run isdigit()

Concatenate ",this,that" to the end of test_string. Use the split function to return a tuple of parts using "," as the separator and print as a **tuple**
   
"""

if __name__ == "__main__":
    test_string = "RaDish8"
    print test_string.index('D')
    print test_string.isalnum()
    ish = test_string[test_string.index('D') + 1:test_string.index('8')]
    print ish.isalpha()
    dig = test_string[-1:]
    print dig.isdigit()

    print tuple(test_string.split(','))
