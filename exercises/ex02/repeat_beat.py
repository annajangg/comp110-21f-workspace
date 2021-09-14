"""Repeating a beat in a loop."""

__author__ = "730411065"


# Begin your solution here...
beat: str = str(input("What beat do you want to repeat? "))
rep: int = int(input("How many times do you want to repeat it? "))
final_beat: str = beat

i: int = 0

if rep <= 0:
    print("No beat...")
else:
    while i < rep:
        final_beat = final_beat + " " + beat
        i = i + 1
print(final_beat)

# could also define a variable as "" and just add onto that
# also could use while loop in the if statement