"""Counting letters in a string."""

__author__ = "730411065"


# Begin your solution here...
letter: str = str(input("What letter do you want to search for?: "))
word: str = str(input("Enter a word: "))
i: int = 0
count: int = 0

while i < len(word):
    if letter == word[i]:
        count = count + 1
    else:
        pass
    i = i + 1

print("Count: " + str(count))