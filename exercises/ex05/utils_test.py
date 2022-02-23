"""Testing List Utilities."""

__author__: str = "730394362"


from ex05.utils import only_evens
from ex05.utils import sub
from ex05.utils import concat


def test_only_evens_use_many_items() -> None:
    """Tests the only_evens function when given a range for a list containing many items."""
    assert only_evens(0, 24)


def test_only_evens_use_edge_empty() -> None:
    """Tests the only_evens function when given an empty range."""
    assert only_evens(0, 0)


def test_only_evens_use_single_item() -> None:
    """Tests the only_evens function by providing a range with only one item."""
    assert only_evens(0, 1)


def test_sub_use_regular() -> None:
    """Tests the sub function when given a list and a start and end index within the length of a the original list."""
    assert sub([0, 0, 0, 1, 1, 1, 0, 0, 0], 2, 7)


def test_sub_edge_empty() -> None:
    """Test the sub function when given an empty list."""
    assert sub([], 1, 2)


def test_sub_same_start_end() -> None:
    """Tests the sub function when given the same start and end integers."""
    assert sub([0, 1, 2, 3, 4, 5], 3, 3)


def test_concat_use_one_empty() -> None:
    """Tests the concat function when one of the lists is empty."""
    assert concat([], [0, 1, 2, 3])


def test_concat_edge_empty() -> None:
    """Tests the concat function when both of the given lists are empty."""
    assert concat([], [])


def test_concat_use_regular() -> None:
    """Test the concat function when given two lists."""
    assert concat([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
    
