"""Testing the dictionary functions created in Exercise 06."""

__author__: str = "730394362"
from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert_regular_use(given_dict: dict[str, str]) -> None:
    assert invert({'black': 'cat', 'brown': 'dog', 'red': 'fox', 'gray': 'squirrel'}) == {'cat': 'black', 'dog': 'brown', 'fox': 'red', 'squirrel': 'gray'}


def test_invert_empty_dict(given_dict: dict[str, str]) -> None:
    assert invert({}) == {}


def test_invert_use(given_dict: dict[str, str]) -> None:
    assert invert


def test_favorite_color_empty_dict(colors: dict[str, str]) -> None:
    assert favorite_color({}) == {}


def test_favorite_color_regular_use(colors: dict[str, str]) -> None:
    assert favorite_color({'jess': 'purple', 'grace': 'purple', 'katy': 'green'}) == "purple"


def test_favorite_color_tie(colors: dict[str, str]) -> None:
    assert favorite_color({'sav': 'red', 'rhiannon': 'green', 'cece': 'red', 'emi': 'green'}) == "red"


def test_count_regular_use(input: list[str]) -> None:
    assert count(['usa', 'norway', 'usa', 'germany', 'germany', 'japan', 'usa', 'usa']) == {'usa': 4, 'norway': 1, 'germany': 2, 'japan': 1}


def test_count_empty(input: list[str]) -> None:
    assert count([]) == {}


def test_count_use(input: list[str]) -> None:
    assert count()