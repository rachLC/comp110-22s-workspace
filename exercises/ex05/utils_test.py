"""Testing List Utilities."""

__author__: str = "730394362"


from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_use_many_items() -> None:
    """Tests the only_evens function when given a list containing many items."""
    assert only_evens([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8]


def test_only_evens_use_edge_empty() -> None:
    """Tests the only_evens function when given an empty list."""
    assert only_evens([]) == []


def test_only_evens_use_single_item() -> None:
    """Tests the only_evens function by providing a list with only one item."""
    assert only_evens([2]) == [2]


def test_sub_use_regular() -> None:
    """Tests the sub function when given a list and a start and end index within the length of a the original list."""
    assert sub([0, 1, 2, 3, 4, 5], 2, 5) == [2, 3, 4]


def test_sub_edge_empty() -> None:
    """Test the sub function when given an empty list."""
    assert sub([], 1, 2) == []


def test_sub_same_start_end() -> None:
    """Tests the sub function when given start and end integers that result in a one item list."""
    assert sub([0, 1, 2, 3, 4, 5], 3, 4) == [3]


def test_concat_use_one_empty() -> None:
    """Tests the concat function when one of the lists is empty."""
    assert concat([], [0, 1, 2, 3]) == [0, 1, 2, 3]


def test_concat_edge_empty() -> None:
    """Tests the concat function when both of the given lists are empty."""
    assert concat([], []) == []


def test_concat_use_regular() -> None:
    """Test the concat function when given two lists."""
    assert concat([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    
