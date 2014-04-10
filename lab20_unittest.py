#!/usr/bin/env python2
# -*- coding: utf-8 -*-

""" 

:mod:`lab20_unittest` --- Module unittest
============================================

#. Create two new exception types: EvenIntegerError and NegativeIntegerError.

#. Create a new class called PositiveOddInt that inherits from **int** and allows one argument during instance creation: the initial value. Save the initial value as the instance attribute *value*, or default to 1 if not given. 

#. Write a __str__() method that returns the class name, the lab number ("Lab20"), the address of the object in memory, and the value of the object.
 
#. This class only supports positive, even integers, so check the initial value. Override the special methods for *add* and *subtract* to check for illegal values and raise the appropriate exception.

#. Override __pow__() to raise a NotImplementedError instead of doing the exponentiation.

#. Create a class TestPositiveOddInt that uses unittest.TestCase as a base class, and implement test cases to verify basic operation of PositiveOddInt as well as the exceptions it raises. Use the built in test runner unittest.main() to test your new class.


"""

class EvenIntegerError(object):
    pass



class NegativeIntegerError(object):
    pass


class PositiveOddInt(int):
    """ A class that does implements extends int """
    def __init__(self, initial_val=1):
        self._validate



