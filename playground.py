from valids import valid
from valids.exceptions import ValueValidationError
from valids.typing import Int16

try:
    valid(
        dtype=Int16,
        v=12_123,
    ).equal(
        other=12_123,
    ).multiple_of(
        of=3,
    ).less_than(
        other=100_000,
    ).greater_than(
        other=10_000,
    )
except ValueValidationError as e:
    print(f"Value didn't pass validation. {e}")
