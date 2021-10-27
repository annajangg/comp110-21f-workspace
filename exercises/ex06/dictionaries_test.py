"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730411065"


def test_invert_letters() -> None:
    """Tests if the letters are inverted."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_words() -> None:
    """Tests if the words are inverted."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_duplicate() -> None:
    """Tests if KeyError comes up if there are duplicate values."""
    assert invert({}) == {}


def test_favorite_color_given() -> None:
    """Tests if most frequent color appears."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_another() -> None:
    """Tests if most frequent color appears."""
    assert favorite_color({"Anna": "pink", "Lila": "blue", "Mathangi": "pink"}) == "pink"


def test_favorite_color_tie() -> None:
    """Tests if first most frequent color appears if there are multiple frequent colors."""
    assert favorite_color({"Maddee": "yellow", "Alex": "blue", "Mitchell": "blue", "Addie": "yellow"}) == "yellow"


def test_favorite_color_same() -> None:
    """Tests if most frequent color appears if all colors are the same."""
    assert favorite_color({"Ruth": "green", "Katherine": "green", "Kyal": "green"}) == "green"


def test_count_first() -> None:
    """Tests if function works."""
    assert count(["1", "1", "1", "5", "5", "3", "1", "3", "3", "1", "4", "4", "4", "2", "2", "2", "2"]) == {"1": 5, "2": 4, "3": 3, "4": 3, "5": 2}


def test_count_second() -> None:
    """Tests if function works."""
    assert count(["5", "5", "5", "1", "1", "2", "5", "2", "2", "5", "4", "4", "4", "3", "3", "3", "2"]) == {"1": 2, "2": 4, "3": 3, "4": 3, "5": 5}


def test_count_third() -> None:
    """Tests if function works."""
    assert count(["1", "2", "3", "4", "5"]) == {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
