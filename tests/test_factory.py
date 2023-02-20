"""Test validator factory."""
from typing import Any, Type, Union

import pytest

from valids.factory import valid
from valids.typing import Int8, Int16, Int32, Int64
from valids.validators import (
    Int8TypeValidator,
    Int16TypeValidator,
    Int32TypeValidator,
    Int64TypeValidator,
)


@pytest.mark.parametrize(
    argnames=[
        "dtype",
        "value",
        "expected_validator",
    ],
    argvalues=[
        (
            Int8,
            10,
            Int8TypeValidator,
        ),
        (
            Int16,
            10,
            Int16TypeValidator,
        ),
        (
            Int32,
            10,
            Int32TypeValidator,
        ),
        (
            Int64,
            10,
            Int64TypeValidator,
        ),
    ],
)
def test_factory_validator_building(
    dtype: Union[Type[Int8], Type[Int16]],
    value: Any,
    expected_validator: Union[
        Type[Int8TypeValidator],
        Type[Int32TypeValidator],
        Type[Int16TypeValidator],
        Type[Int64TypeValidator],
    ],
) -> None:
    """Test factory returns correct type of validator."""
    validator = valid(dtype=dtype, v=value)
    assert isinstance(validator, expected_validator)


def test_factory_failure_when_not_handled_dtype() -> None:
    """Test factory fails when not handled dtype is requested."""
    with pytest.raises(RuntimeError):
        valid(dtype=Any, v=...)  # type:ignore[call-overload]
