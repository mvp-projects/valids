"""Validator factory method."""
from typing import Any, Type, overload

from valids.base import IValidator
from valids.typing import Int8, Int16, ValidsDataType
from valids.validators.numeric import Int8Validator, Int16Validator


@overload
def valid(v: Any, dtype: Type[Int8]) -> Int8Validator:
    ...


@overload
def valid(v: Any, dtype: Type[Int16]) -> Int16Validator:
    ...


def valid(v: Any, dtype: ValidsDataType) -> IValidator:
    """Value is the entrypoint of the eager module."""
    if dtype == Int8:
        return Int8Validator(value=v)

    if dtype == Int16:
        return Int16Validator(value=v)

    raise RuntimeError("No datatype handled.")
