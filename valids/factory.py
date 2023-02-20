"""Validator factory method."""
from typing import Any, Type, Union, overload

from valids.base import IValidator
from valids.typing import Int8, Int16, Int32, Int64, UInt8, UInt16, UInt32, UInt64
from valids.validators import (
    Int8TypeValidator,
    Int16TypeValidator,
    Int32TypeValidator,
    Int64TypeValidator,
    UInt8TypeValidator,
    UInt16TypeValidator,
    UInt32TypeValidator,
    UInt64TypeValidator,
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


def valid(  # noqa: PLR0911
    dtype: Union[
        Type[Int8],
        Type[Int16],
        Type[Int32],
        Type[Int64],
        Type[UInt8],
        Type[UInt16],
        Type[UInt32],
        Type[UInt64],
    ],
    v: Any,
) -> IValidator:
    """Value is the entrypoint of the eager module."""
    if dtype == Int8:
        return Int8TypeValidator(value=v)
    if dtype == UInt8:
        return UInt8TypeValidator(value=v)
    if dtype == Int16:
        return Int16TypeValidator(value=v)
    if dtype == UInt16:
        return UInt16TypeValidator(value=v)
    if dtype == Int32:
        return Int32TypeValidator(value=v)
    if dtype == UInt32:
        return UInt32TypeValidator(value=v)
    if dtype == Int64:
        return Int64TypeValidator(value=v)
    if dtype == UInt64:
        return UInt64TypeValidator(value=v)

    raise RuntimeError(f"{str(dtype)} is not being handled by the factory.")
