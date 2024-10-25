#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:45:30 2024

@author: winsicheng
"""

#CREATE A DICTIONARY WITH THE FOLLOWING QUESTIONS AND ITS CORRECT ANSWER
questions_answers = {
    "France?": "Paris",
    "Italy?": "Rome",
    "Spain?": "Madrid",
    "Germany?": "Berlin",
    "United Kingdom?": "London",
    "Sweden?": "Stockholm",
    "Norway?": "Oslo",
    "Denmark?": "Copenhagen",
    "Finland?": "Helsinki",
    "Greece?": "Athens"
}

def quiz(): #DEFINE THE QUIZ 
    for country, capital in questions_answers.items():
        question = input(f"What is the capital of {country}?") # ASK FOR USER INPUT
        if question == capital: # USING IF ELSE STATEMENTS TO GIVE FEEDBACK 
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {capital}")

quiz()

