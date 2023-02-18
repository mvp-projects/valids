"""Test something."""

from valids import valid
from valids.typing import Int8


def test_something() -> None:
    """Test something."""
    valid(
        v=30,
        dtype=Int8,
    ).multiple_of(
        of=3,
    ).greater_than(
        other=9,
    ).less_than(
        other=500,
    ).equal(
        other=30,
    )
