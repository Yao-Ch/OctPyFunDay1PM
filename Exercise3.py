# -*- coding: utf-8 -*-
"""
Write a Python script that implements the "Guess the Number" game.
The script will generate of a random integral number (use the module random) 
from 1 to 100, and ask you to guess it.
The script will tell you if each guess is too high or too low.
You win if you can guess the number within six tries.

As long as the user does not find the secret number and as long he(she) has 
not provided 6 values we "iterate" (with the help of a while loop)

In each iteration we:
    prompt the user for a value (using input())
    compare this value with the secret number (with the help of if/elif/else and
                                               == < >, ...)
    print an appropriate message
    increment the current number of attempts to guess the secret number
    
At the end, if the secret number is not found, we print it's value
"""

import random

secret=random.randint(1,100)

print(secret)

currentNumberOfAttempts=0
currentValue=0

while secret != currentValue and currentNumberOfAttempts < 6:
    currentValue=input(f"Enter an int in the range [1,100] ({currentNumberOfAttempts+1}/6): ")
    currentValue=int(currentValue)
    if currentValue == secret:
        print ("Bingo ! You've found the secret number")
    elif currentValue > secret:
        print("Too large !")
    elif currentValue < secret:
        print("Too small")
    currentNumberOfAttempts += 1
   # currentNumberOfAttempts = currentNumberOfAttempts + 1
    
if secret != currentValue:
    print("The secret number was:", secret)
    
    