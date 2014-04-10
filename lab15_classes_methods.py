#!/usr/bin/env python2
# -*- coding: utf-8 -*-

""" 

:mod:`lab15_classes_methods` --- Classes and Methods
====================================================

Create a new class called **MyLabClass** with new class variables 
   called *my_x* = 1, *_my_private_x* = 11, *__my_very_private_x* = 111

What special function gets called when constructing a new class instance?

Write that function and accept one argument. Is that the only argument you must plan for? Store the argument in *self.my_x*

Create a new method in **MyLabClass** called *my_fun* that creates variable *my_x* = 33 and returns it

Create a new instance of **MyLabClass** passing in 7. Call *my_fun* on the instance and print it. 

Print the class variables. Print the results of dir(**MyLabClass**) to verify. 

In lottery_drawing.py: 

 #. Create (3) custom Exception classes: **InvalidSelectionCount**, **InvalidSelectionType**,
 and **InvalidSelectionRange**
 #. Create a new class called **LotteryDrawing**
 #. **__init__()** should initialize instance variables for *max_ball_number* (from command arguments),
 *years* (from command arguments), *picks* (a set from command arguments, or hard code),
 *elapsed* (a float), *results* (an empty dict) , *drawings* (years * 104), and *quick_pick* = False
 #. Create a private **_pick_numbers()** method that returns a set of random numbers
 (equal to the number of picks per drawing) in the range of 1 to *max_ball_number*.
 Choose a function from the **random** module for this
 #. Create a public **run_simulation()** method that runs the simulation as follows: 
    1) Generate *drawings* simulated drawings per year by calling method **_pick_numbers()**
    2) For each drawing, match the set of user selected numbers (picks) against the simulation numbers
    and update the **results** dict. The **results** dict has 7 keys (0 - 6) where the associated values
    are the number of matches e.g. if a drawing set matches two of the user selected set, key 2 is
    incremented
    3) Compute elapsed time and store in *elapsed* 
 #. Move the constants in **lotto.py** to a new module **lotto_constants.py**. What do you have to do to
 see them?
 #. Optionally create a private **_validate()** method to validate the user inputs to raise the custom
 execeptions if necessary

In lotto.py: 
 #. Instantiate an instance of LotteryDrawing 
 #. Call its **run_simulation()** method
 #. Modify **print_results()** to take a LotteryDrawing object as the argument 
    (instead of the dict in lab10). Call **print_results()** method
 #. Test lotto module with -h, then with actual arguments

"""

class MyLabClass(object):
    my_x = 1
    _my_private_x = 11
    __my_very_private_x = 111

    def __init__(self, my_x):
        self.my_x = my_x

    def my_fun(self):
        my_x = 33
        return  my_x

if __name__ == "__main__":
    foo = MyLabClass(7)
    print foo.my_fun()

    print dir(MyLabClass)

    import lotto

    lottery = lotto.LotteryDrawing(54, 1, set([15, 44, 34, 45, 32, 12]))
    lottery.run_simulation()
    lottery.print_results(lottery)