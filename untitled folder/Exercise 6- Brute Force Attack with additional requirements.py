#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 23:48:07 2024

@author: winsicheng
"""

# CREATE A VARIABLE OF THE NUMBER OF ATTEMPTS

attempts = 5

# Use a while loop to keep asking the password until it is correct but only until 5 tries 

while attempts > 0:

  

    password = input("Enter the password: ")



    if password == "12345":

        print("Correct password!") #create a if else statement that prints access is granted if it is the password

        break

    else:

        print("Incorrect password. You have", attempts - 1, "attempts remaining.")

        attempts -= 1



if attempts == 0:

    print(" Authorities have been alerted.") #IF IT HAS REACHED MORE THAN 5 ATTEMPTS LET THE USERS KNOW THAT AUTHORITIES WOULD BE ALERTED BY PRINTING