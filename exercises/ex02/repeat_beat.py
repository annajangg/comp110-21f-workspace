"""Repeating a beat in a loop."""

__author__ = "730411065"


# Begin your solution here...
beat: str = str(input("What beat do you want to repeat? "))
rep: int = int(input("How many times do you want to repeat it? "))

if rep > 0:
    print((beat + " ") * (rep - 1) + beat)
    rep = rep - 1
else:
    print("No beat...")