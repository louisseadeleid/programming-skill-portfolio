#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 23:38:09 2024

@author: winsicheng
"""

DAYS = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


#CREATE A DICTIONARY USING CURLY BRACKETS AND ASSIGN EACH MONTH TO ITS DESIGNATED AMOUNT OF DAYS

# CREATE A VARIABLE THAT TAKES USER INPUT 
monthnum = int(input("Enter the month number (1-12): "))

# USING IF ELSE TO CHECK IF THE INPUTS GIVEN ARE ONLY FROM 1-12 AND USE ELSE TO TELL THE USER THAT ITS AN ERROR
if monthnum < 1 or monthnum > 12:
    print("ERROR! Enter a number from 1 and 12!")
else:
    # USING IF TO CHECK A CONDITION TO FIGURE OUT IF ITS A LEAP YEAR OR NOT
    if monthnum == 2:
        leapyear = input("Is it a leap year? ").lower()
        if leapyear == "yes":
            DAYS[2] = 29
      
    
    print(f"There are {DAYS[monthnum]} days in the month numner {monthnum}.") # THEN CREATE A VARIABLE THAT PRINTS THE OUTPUT AFTER USER INPUT