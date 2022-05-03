#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    savenum = number % 10 * -1
if number >= 0:
    savenum = number % 10

if savenum % 10 > 5:
    print(f"Last digit of {number} is {savenum} and is greater than 5")
if savenum % 10 == 0:
    print(f"Last digit of {number} is {savenum} and is 0")
if savenum % 10 < 6 and number % 10 != 0:
    print(f"Last digit of {number} is {savenum} and is less than 6 and not 0")
