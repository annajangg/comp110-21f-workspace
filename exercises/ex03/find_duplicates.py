"""Finding duplicate letters in a word."""

__author__ = "730411065"

word: str = input("Enter a word: ")
i: int = 0
dup: bool = False

while i < len(word):
    char: str = word[i]
    j: int = i + 1
    while j < len(word):
        if word[j] == char:
            dup: bool = True
        else:
            dup = dup
        j = j + 1
    i = i + 1

print("Found duplicate: " + str(dup))
