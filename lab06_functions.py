#!/usr/bin/env python2
# -*- coding: utf-8 -*-

""" 

:mod:`lab06_functions` -- Functions 
===================================

Read the online documentation for the **argparse** module

What is the difference between options and arguments?

In lotto.py. create an new argparse object with description *Virtual Lottery Simulation Engine*
(We have not covered classes yet, so just copy/paste the argparse example code)

 **import argparse** 
 ...
 **args = parser.parse_args()** 

Accept 2 command line arguments setting dest, default, and help options:
 #. -b (also --max_ball_num) which is the number of lotto balls. Default = 54
 #. -y (also --years) which is the number of years of drawings to run. Default = 1
 
Hint: You want something similar to the '--sum' in the example code.

Print the resulting **args** object. How does dest relate to args?

Test the **-h** option, then **-b** and **-y** together and separately

Define a new function called **calc_odds()** that accepts 2 arguments:
 #. max_ball_num (default DEFAULT_NUM_BALLS)
 #. num_picks (default = DEFAULT_NUM_PICKS)

Have calc_odds() return the odds of winning (getting all num_picks choices correct) where order is not significant: 
 #. Create a new list using range()
 #. Return the last DEFAULT_NUM_PICKS numbers multiplied together 

"""

import lotto
def calc_odds(max_num_balls=lotto.DEFAULT_NUM_BALLS, num_picks=lotto.DEFAULT_NUM_PICKS):
    # balls = range(1, max_num_balls+1)
    # odds = 1
    # while num_picks:
    #     odds *= len(balls)
    #     balls.pop(num_picks-1)
    #     num_picks -= 1
    # return odds
    rng = []
    for i in range(num_picks):
        rng.append(max_num_balls-i)
    odds = reduce(lambda a, b: a*b, rng)
    return odds

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Virtual Lottery Simulation Engine')
    parser.add_argument('-b', '--max_ball_num', type=int, dest='max_ball_num', default=lotto.DEFAULT_NUM_BALLS,
                       help='The number of lotto balls (default '+str(lotto.DEFAULT_NUM_BALLS)+')')
    parser.add_argument('-y', '--years', type=int, dest='years', default=lotto.DEFAULT_YEARS,
                       help='The number of drawings in a year (default '+str(lotto.DEFAULT_YEARS)+')')

    args = parser.parse_args()

    print lotto.calc_odds(args.max_ball_num)
