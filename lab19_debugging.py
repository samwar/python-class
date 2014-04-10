#!/usr/bin/env python2
# -*- coding: utf-8 -*-

""" 

:mod:`lab19_debugging` --- Debugging
====================================

If necessary, install pudb at http://pypi.python.org/pypi/pudb 

Write a simple module that does 10 assignments to different variables, and calls a function. The function has 5 assignments and one print, and returns one of the variables. Have 5 lines after the function call.

Add the required import and place the set_trace() call as the first executable statement 

Run your module in ipython and ctrl-p to set your preferences. Use the cursor control keys to navigate.

Type "?" and review the commands available. 

Set a break point at the function call

Use step over ("n"), step into ("s"), return ("r"), and run-to-cursor ("t").  Observe the stack and variables screen. Move cursor to the Variable screen and scroll to see all variables.  

Step into the function. Notice the namespace changes. After the print, use the output("o") command to see the result. 

Use the search facility ("/") to find your function.

Use the "+" and "-" commands. What do they do? Now play with the "_" and "=" commands.  What do they do?

Use "V", "B", and "S" commands on the sub-screens. Use "[" and "]" commands on each subscreen. What happens? Finally, quit("q")

"""

