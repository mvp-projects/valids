"""Valids custom type annotations."""

from typing import Any, TypeAlias, Union

ValidsDataType: TypeAlias = Union["DataTypeClass", "DataType"]

__all__ = [
    "Int8",
    "Int16",
    "Int32",
    "Int32",
    "Float32",
    "Float64",
    "Boolean",
    "Date",
    "Utf8",
    "DateTime",
]


class DataTypeClass(type):
    """Metaclass for nicely printing DataType classes."""

    def __repr__(cls) -> str:  # noqa: D105
        return cls.__name__


class DataType(metaclass=DataTypeClass):
    """Base class for all valids data types."""

    def __new__(  # type:ignore[misc]  # noqa: D102
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> ValidsDataType:
        if args or kwargs:
            return super().__new__(cls=cls)
        return cls


class _NumericType(DataType):
    """Base class for numeric data types."""


class _IntegralType(_NumericType):
    """Base class for integral data types."""


class _FractionalType(_NumericType):
    """Base class for fractional data types."""


class _TemporalType(DataType):
    """Base class for temporal data types."""


class Int8(_IntegralType):
    """8-bit signed integer type."""


class Int16(_IntegralType):
    """16-bit signed integer type."""


class Int32(_IntegralType):
    """32-bit signed integer type."""


class Int64(_IntegralType):
    """64-bit signed integer type."""


class UInt8(_IntegralType):
    """8-bit unsigned integer type."""


class UInt16(_IntegralType):
    """16-bit unsigned integer type."""


class UInt32(_IntegralType):
    """32-bit unsigned integer type."""


class UInt64(_IntegralType):
    """64-bit unsigned integer type."""


class Float32(_FractionalType):
    """32-bit floating point type."""


class Float64(_FractionalType):
    """64-bit floating point type."""


class Boolean(DataType):
    """Boolean type."""


class Utf8(DataType):
    """UTF-8 encoded string type."""


class Date(_TemporalType):
    """Calendar date type."""


class DateTime(_TemporalType):
    """Calendar date type."""
