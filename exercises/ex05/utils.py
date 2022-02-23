"""Ex05 - 'list' Utility Functions."""

__author__: str = "730394362"


def only_evens(min: int, max: int) -> list[int]:
    """Create a list of even numbers from a given range."""
    xs: list[int] = list()
    i: int = (min // 2) * 2
    while i <= max:
        xs.append(i)
        i += 2 
    return xs


def sub(a_list: list, start: int, end: int) -> list[int]:
    """Create a subset list of a given list."""
    sub_list: list[int] = list()
    i = start
    real_end = end - 1
    while i <= real_end:
        sub_list += a_list[i]
        i += 1
    return sub_list


def concat(first_list: list, second_list: list) -> list[int]:
    """Concatenate two given lists into one."""
    full_list: list[int] = list()
    i: int = 0
    while i < len(first_list):
        full_list += first_list[i]
        i += 1
    n: int = 0
    while n < len(second_list):
        full_list += second_list[n]
        n += 1
    return full_list
