#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:39:44 2024

@author: winsicheng
"""

#CREATE FUNCTION THAT IS NAMED HELLO
def hello():
    print("Hello")
#CREATE ANOTHER FUNCTION INSIDE THE FUNCTION HELLO AND WHEN IT IS EXECUTED THE FUNCTION HELLO IS ALSO RUNNED
def main():
    hello()
    
#CREATE IF STATEMENT THAT EVALUATES IF IT IS TRUE AND IF IT IS THE FUNCTION MAIN IS CALLED 

if __name__ == "__main__": 

    main()