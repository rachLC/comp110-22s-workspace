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
    a_list: list[int] = list()





def concat(first_list: list, second_list: list) -> list[int]:
    """Concatenate two given lists into one."""
    full_list: str = ""
    first: str = first_list
    second: str = second_list
    full_list += first  
    full_list += second
    return full_list

