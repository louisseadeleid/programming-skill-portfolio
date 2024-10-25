#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:19:44 2024

@author: winsicheng
"""
# create a function named is_even that takes the parameter number
def is_even(number):
    return "EVEN" if number % 2 == 0 else "ODD" # CREATE A FUNCTION THAT EVALUATES IF IT IS ODD OR EVE

#create another function in this case it is named "real" that serves as the main input for users
def real():
    number = int(input("WHATS YOUR NUMBER? "))
    result = is_even(number) #it calls the is even function created earlier to make sure the result is even
    print(result) #print the results

if __name__ == "__main__":
    real()
