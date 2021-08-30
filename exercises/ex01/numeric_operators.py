"""Exercise 1: Numeric Operators."""
__author__ = "730411065"

left_hand: int = int(input("What number do you want to compute in the left hand side? "))
right_hand: int = int(input("What number do you want to compute in the right hand side? "))
print("Left-hand side: " + str(left_hand))
print("Right-hand side: " + str(right_hand))
exponent: int = left_hand ** right_hand
print(str(left_hand) + " ** " + str(right_hand) + " is " + str(exponent))
division: float = left_hand / right_hand
print(str(left_hand) + " / " + str(right_hand) + " is " + str(division))
integer: int = left_hand // right_hand
print(str(left_hand) + " // " + str(right_hand) + " is " + str(integer))
remainder: int = left_hand % right_hand
print(str(left_hand) + " % " + str(right_hand) + " is " + str(remainder))
