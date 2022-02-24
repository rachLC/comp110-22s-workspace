"""Ex05 - 'list' Utility Functions."""

__author__: str = "730394362"


def only_evens(give_list: list[int]) -> list[int]:
    """Create a list of even numbers from a given range."""
    xs: list[int] = list()
    for i in give_list:
        if i % 2 == 0:
            xs.append(i)
    return xs


def sub(a_list: list, start: int, end: int) -> list[int]:
    """Create a subset list of a given list."""
    sub_list: list[int] = list()
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    if len(a_list) == 0:
        return []
    if start > len(a_list):
        return []
    if end <= 0:
        return []
    while start < end:
        sub_list.append(a_list[start])
        start += 1
    return sub_list


def concat(first_list: list, second_list: list) -> list[int]:
    """Concatenate two given lists into one."""
    i: int = 0
    for i in second_list:
        first_list.append(i)
    return first_list
