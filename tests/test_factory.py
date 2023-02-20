"""Test validator factory."""
from typing import Any

import pytest

from valids.base import IValidator
from valids.factory import valid
from valids.typing import (
    Boolean,
    DataType,
    Int8,
    Int16,
    Int32,
    Int64,
    UInt8,
    UInt16,
    UInt32,
    UInt64,
    Utf8,
)
from valids.validators import (
    BooleanTypeValidator,
    Int8TypeValidator,
    Int16TypeValidator,
    Int32TypeValidator,
    Int64TypeValidator,
    UInt8TypeValidator,
    UInt16TypeValidator,
    UInt32TypeValidator,
    UInt64TypeValidator,
    Utf8TypeValidator,
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
            UInt8,
            10,
            UInt8TypeValidator,
        ),
        (
            Int16,
            10,
            Int16TypeValidator,
        ),
        (
            UInt16,
            10,
            UInt16TypeValidator,
        ),
        (
            Int32,
            10,
            Int32TypeValidator,
        ),
        (
            UInt32,
            10,
            UInt32TypeValidator,
        ),
        (
            Int64,
            10,
            Int64TypeValidator,
        ),
        (
            UInt64,
            10,
            UInt64TypeValidator,
        ),
        (
            Boolean,
            False,
            BooleanTypeValidator,
        ),
        (
            Utf8,
            "asd",
            Utf8TypeValidator,
        ),
    ],
)
def test_factory_validator_building(
    dtype: DataType,
    value: Any,
    expected_validator: IValidator,
) -> None:
    """Test factory returns correct type of validator."""
    validator = valid(dtype=dtype, v=value)  # type:ignore[call-overload]
    assert isinstance(validator, expected_validator)  # type:ignore[arg-type]


def test_factory_failure_when_not_handled_dtype() -> None:
    """Test factory fails when not handled dtype is requested."""

    class NotSupportedDataType(DataType):
        ...

    with pytest.raises(RuntimeError):
        valid(dtype=NotSupportedDataType, v=...)  # type:ignore[call-overload]
