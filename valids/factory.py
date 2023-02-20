"""Validator factory method."""
from typing import Any, Type, Union, overload

from valids.base import IValidator
from valids.typing import Int8, Int16, Int32, Int64
from valids.validators.numeric import (
    Int8TypeValidator,
    Int16TypeValidator,
    Int32TypeValidator,
    Int64TypeValidator,
)


@overload
def valid(dtype: Type[Int8], v: int) -> Int8TypeValidator:
    ...


@overload
def valid(dtype: Type[Int16], v: int) -> Int16TypeValidator:
    ...


@overload
def valid(dtype: Type[Int32], v: int) -> Int32TypeValidator:
    ...


@overload
def valid(dtype: Type[Int64], v: int) -> Int64TypeValidator:
    ...


def valid(
    dtype: Union[
        Type[Int8],
        Type[Int16],
        Type[Int32],
        Type[Int64],
    ],
    v: Any,
) -> IValidator:
    """Value is the entrypoint of the eager module."""
    if dtype == Int8:
        return Int8TypeValidator(value=v)
    if dtype == Int16:
        return Int16TypeValidator(value=v)
    if dtype == Int32:
        return Int32TypeValidator(value=v)
    if dtype == Int64:
        return Int64TypeValidator(value=v)
    raise RuntimeError(f"{dtype} is not being handled by the factory.")
