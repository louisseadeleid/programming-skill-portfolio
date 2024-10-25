#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 23:40:48 2024

@author: winsicheng
"""

#CREATE VARIABLE TO GET THE USERS INPUT
name = input("What is your name? ")
hometown = input("Where is your hometown?")
age = int(input("Enter your age: "))

# CREATE A DICTIONARY WITH CURLY BRACKETS TO STORE THE INPUTS
person = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# USING A FUNCTION, PRINT THE FOLLOWING INPUTS
print(f"Name: {person['name']}\nHometown: {person['hometown']}\nAge: {person['age']}")