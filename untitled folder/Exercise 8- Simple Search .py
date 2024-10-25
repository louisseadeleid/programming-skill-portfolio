#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:02:35 2024

@author: winsicheng
"""

names = ["Jake",
          "Zac",
          "Ian",
          "Ron",
          "Sam",
          "Dave"]

ask_question = input("Search for the name:")

if ask_question in names:
    print(f'{ask_question} is in the list!')
else:
    print('Name is not in the list!')
    