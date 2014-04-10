#!/usr/bin/env python2
# -*- coding: utf-8 -*-

""" 

:mod:`lab07_built_in_functions` -- Built-ins
===================================================

Reference the built-in functions on p.102 of the pocket reference

Create a new variable *my_var* and assign it a value. Set *my_var_2* = *my_var*

Is the id() of *my_var* the same as the id() of *my_var_2*?

Create a new tuple *my_tuple* of integers and print the result of running 
   sum() and max() on it

What function would return the length of *my_tuple*? Print the result

Print the length of the resulting object using set() on [2, 18, 77, 3, 2]

Use zip() and dict() to create a new dictionary from two tuples. The first tuple has the keys, the other has the values.

Create a function that takes 2 arguments and returns their product. Use map() with two iterables and the product function. Print the result.

Create a function that takes 1 integer argument and returns True if odd, else False. Use filter() and that function to consume a list of even and odd integers. Print the result.

Create a function that takes 2 arguments and returns twice their sum. Use  reduce() and that function on an iterable. Print the result.

What does locals() do and what data type is it? Print your locals()

"""


def product(x, y):
    return x * y


def even_odd(i):
    return True if i % 2 == 0 else False


def double_sum(x, y):
    return (x + y) * 2


if __name__ == "__main__":
    my_var = 4
    my_var_1 = my_var
    print 'id of my_var' + str(id(my_var))
    print 'id of my_var_1' + str(id(my_var_1))

    my_tuple = tuple([1, 2, 3])
    print 'my_tuple: ' + str(my_tuple)
    print 'sum my_tuple: ' + str(sum(my_tuple))
    print 'max my_tuple: ' + str(max(my_tuple))
    print 'len my_tuple: ' + str(len(my_tuple))

    print str(len(set([2, 18, 77, 3, 2])))

    keys = tuple([1, 2, 3])
    values = tuple(['a', 'b', 'c'])
    zipped_tup = dict(zip(keys, values))
    print zipped_tup
    print map(product, [1, 2, 3], [4, 5, 6])
    print filter(even_odd, [1, 2, 3, 4])
    print reduce(double_sum, [1, 2, 3, 4])
    print reduce(double_sum, [1, 2, 3])

    #print locals()



