"""Drawing forests in a loop."""

__author__ = "730411065"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))
str_tree: str = ""
i: int = 0

# while i <= depth:
# print(TREE * i)
# i = i + 1

while i < depth:
    str_tree = str_tree + TREE
    print(str_tree)
    i = i + 1
