#!/usr/bin/python3
for a in range(1, 101):
    if a % 3 == 0 or a % 5 == 0:
        if a % 3 == 0:
            print("Fizz", end="")
            if a % 5 == 0:
                print("Buzz", end="")
    else:
        print(f"{a}", end="")
    if a != 100:
        print(" ", end=" ")
