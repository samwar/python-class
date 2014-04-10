#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""

:mod:`lab01_identifiers_modules` -- Identifiers & Modules 
=========================================================
   
Write the identifier naming conventions for: 
   variables, constants, functions
   
What leading character is used to make a variable private?
   What are the two types of private variables?
   
.. note::

 We will be building a virtual lottery as a lab project.

Create a new module called lotto.py which initializes the following constants:

 #. DRAWS_PER_YEAR = 104
 #. RANDOM_MIX = 20
 #. DEFAULT_NUM_BALLS = 54
 #. DEFAULT_YEARS = 1
 #. DEFAULT_NUM_PICKS = 6

Add at the top:  

::

 #!/usr/bin/env python2
 # -*- coding: utf-8 -*-
 print "DRAWS_PER_YEAR is", DRAWS_PER_YEAR
   
Create another module named lottery_drawing.py with the following:

::

 #!/usr/bin/env python2
 # -*- coding: utf-8 -*-
 import random
 import time
 import lotto_constants

Read the Ipython help on the *edit* and *run* magic commands.

Use *edit* or *run* to execute **lotto.py**. Correct any errors.

"""

if __name__ == "__main__":
    pass
