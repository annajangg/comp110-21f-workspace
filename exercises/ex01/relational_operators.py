"""Exercise 01: Relational Operators."""
__author__ = "730411065"

left_hand: int = int(input("What number do you want to compute in the left hand side? "))
right_hand: int = int(input("What number do you want to compute in the right hand side? "))
print("Left-hand side: " + str(left_hand))
print("Right-hand side: " + str(right_hand))
less_than: bool = left_hand < right_hand
print(str(left_hand) + " < " + str(right_hand) + " is " + str(less_than))
great_equal: bool = left_hand >= right_hand
print(str(left_hand) + " >= " + str(right_hand) + " is " + str(great_equal))
equal: bool = left_hand == right_hand
print(str(left_hand) + " == " + str(right_hand) + " is " + str(equal))
not_equal: bool = left_hand != right_hand
print(str(left_hand) + " != " + str(right_hand) + " is " + str(not_equal))