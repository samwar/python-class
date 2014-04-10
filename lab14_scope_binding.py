#!/usr/bin/env python2
# -*- coding: utf-8 -*-

""" 

:mod:`lab14_scope_binding` --- Scope and Binding
================================================

#. Create a new module called *my_scope.py*

#. Create a new variable in *my_scope* called *my_x* = 3

#. Create a new function in *my_scope* called *my_fun* that creates variable *my_x = 33* and returns it

#. In the mainline code for *my_scope*, print the value of *my_x*, then call *my_fun* and print its return value. Are they the same? Why or why not?

#. Create a new function in *my_scope.py* called *deco* that accepts a single function argument, then defines and returns another function (i.e. def inside a def).  The returned function should call the function passed into *deco* and print its results.

#. Call *deco* within your mainline and send the builtin function globals() as an argument. Run the returned function. Call *deco* again but send locals(). Run the returned function. 

#. Finally, call *deco* with *my_fun* and run the returned function.

"""


def my_fun():
    my_x = 33
    return my_x


def deco(fn):
    def deco1():
        print fn()

    return deco1


if __name__ == "__main__":
    my_x = 3

    print "\ndeco with globals\n"
    deco(globals)()
    print "deco with locals"
    deco(locals)()
    print "\ndeco with my_fun"
    deco(my_fun())
