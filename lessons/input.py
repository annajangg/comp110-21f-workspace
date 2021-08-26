"""A program to demonstrate user input and variables."""

"""variable name: data type =(assignment operator) string."""
user_name: str = input("Who are you? ")
print("Wow, " + user_name + ", you rock!")
print(user_name + " have a great day!")


"""EXample diagram problem."""

age: int = int(input("How old are you? "))
year: int = int(input("What year is it? "))
age_in_2041: int = 2041 - year + age
print("In 2041, you will be " + str(age_in_2041) + ".")

age = age + 1
year = year + 1
print("Next year, in " + str(year) + ", you will be " + str(age) + ".")
