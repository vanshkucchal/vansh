# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 09:38:41 2025

@author: kucch
"""

try:
 n1=int(input("enter any number"))
 y=25/n1
 print(y)
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    print("number required")