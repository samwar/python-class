#!/usr/bin/env python2
#-*-code:utf-8-*-
"""
This module transforms letters starting with vowels into pig latin
"""
__author__ = 'samu6978'

user_input = raw_input("Enter a single word yo!")

if user_input[0].lower() in 'aeiou':
    user_input += 'ly'
elif ord(user_input[0]) % 2 == 0:
    user_input = "eek! "+ user_input
else:
    user_input = user_input[1:] + user_input[0] +'ly'

print user_input