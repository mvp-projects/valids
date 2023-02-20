"""Validator factory method."""
from typing import Any, Dict, Type, overload

from valids.base import IValidator
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


@overload
def valid(dtype: Type[Int8], v: int) -> Int8TypeValidator:
    ...


@overload
def valid(dtype: Type[UInt8], v: int) -> UInt8TypeValidator:
    ...


@overload
def valid(dtype: Type[Int16], v: int) -> Int16TypeValidator:
    ...


@overload
def valid(dtype: Type[UInt16], v: int) -> UInt16TypeValidator:
    ...


@overload
def valid(dtype: Type[Int32], v: int) -> Int32TypeValidator:
    ...


@overload
def valid(dtype: Type[UInt32], v: int) -> UInt32TypeValidator:
    ...


@overload
def valid(dtype: Type[Int64], v: int) -> Int64TypeValidator:
    ...


@overload
def valid(dtype: Type[UInt64], v: int) -> UInt64TypeValidator:
    ...


@overload
def valid(dtype: Type[Boolean], v: bool) -> BooleanTypeValidator:  # noqa: FBT001
    ...


@overload
def valid(dtype: Type[Utf8], v: str) -> Utf8TypeValidator:
    ...


def valid(
    dtype: Type[DataType],
    v: Any,
) -> IValidator:
    """Value is the entrypoint of the eager module."""
    type_to_validator_mapper: Dict[Type[DataType], Type[IValidator]] = {
        Int8: Int8TypeValidator,
        UInt8: UInt8TypeValidator,
        Int16: Int16TypeValidator,
        UInt16: UInt16TypeValidator,
        Int32: Int32TypeValidator,
        UInt32: UInt32TypeValidator,
        Int64: Int64TypeValidator,
        UInt64: UInt64TypeValidator,
        Boolean: BooleanTypeValidator,
        Utf8: Utf8TypeValidator,
    }
    validator = type_to_validator_mapper.get(dtype)
    if validator:
        return validator(value=v)
    raise RuntimeError(f"{str(dtype)} is not being handled by the factory.")
