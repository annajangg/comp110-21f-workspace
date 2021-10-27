"""Practice with dictionaries."""

__author__ = "730411065"

# Define your functions below


def invert(i_dict: dict[str, str]) -> dict[str, str]:
    """Function to invert the entries in a dictionary."""
    inverted: dict[str, str] = {}
    for key in i_dict:
        if i_dict[key] in inverted:
            raise KeyError("There are more than one of the same key.")
        inverted[i_dict[key]] = key
    return inverted
 

def favorite_color(i_fav: dict[str, str]) -> str:
    """Function to give the color that is most popular."""
    counter: dict[str, int] = {}
    for name in i_fav:
        if i_fav[name] in counter:
            counter[i_fav[name]] += 1
        else:
            counter[i_fav[name]] = 1
    most: int = 0
    most_color: str = ""
    for color in counter:
        if counter[color] > most:
            most = counter[color]
            most_color = color
    return most_color


def count(freq: list[str]) -> dict[str, int]:
    """Function to count the frequency the numbers come up."""
    result = {}
    for item in freq:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
