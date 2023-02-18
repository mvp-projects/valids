"""Numeric related validator."""

from typing import Any, Union

from typing_extensions import Self

from valids.base import IValidator


class _NumericTypeValidator(IValidator):
    """Eager validator implementation for numeric values."""

    def __init__(self, value: Any) -> None:
        self.value = value

    def greater_than(self, other: Union[int, float]) -> Self:
        if self.value > other:
            return self
        raise RuntimeError("Validation Error.")

    def greater_equal_than(self, other: Union[int, float]) -> Self:
        if self.value >= other:
            return self
        raise RuntimeError("Validation Error.")

    def less_than(self, other: Union[int, float]) -> Self:
        if self.value < other:
            return self
        raise RuntimeError("Validation Error.")

    def less_equal_than(self, other: Union[int, float]) -> Self:
        if self.value <= other:
            return self
        raise RuntimeError("Validation Error.")


class _IntegralTypeValidator(_NumericTypeValidator):
    """Eager validator implementation for integral data types."""

    def __init__(self, value: Any) -> None:
        super().__init__(value)

    def multiple_of(self, of: int) -> Self:
        """Check integer value is multiple of other value."""
        if self.value % of == 0:
            return self
        raise RuntimeError("Validation Error.")

    def equal(self, other: Union[int, float]) -> Self:
        if self.value == other:
            return self
        raise RuntimeError("Validation Error.")


class _FractionalTypeValidator(_NumericTypeValidator):
    """Eager validator implementation for fractional data types."""


class Int8Validator(_IntegralTypeValidator):
    """Eager validator implementation for 8-bit signed integer type."""

    def __init__(self, value: Any) -> None:  # noqa: D107
        # TODO: An assertion on dataype.
        super().__init__(value)


class Int16Validator(_IntegralTypeValidator):
    """Eager validator implementation for 16-bit signed integer type."""

    def __init__(self, value: Any) -> None:  # noqa: D107
        # TODO: An assertion on dataype.
        super().__init__(value)


class Int32Validator(_IntegralTypeValidator):
    """Eager validator implementation for 32-bit signed integer type."""

    def __init__(self, value: Any) -> None:  # noqa: D107
        # TODO: An assertion on dataype.
        super().__init__(value)


class Int64Validator(_IntegralTypeValidator):
    """Eager validator implementation for 64-bit signed integer type."""

    def __init__(self, value: Any) -> None:  # noqa: D107
        # TODO: An assertion on dataype.
        super().__init__(value)


class UInt8Validator(_IntegralTypeValidator):
    """Eager validator implementation for 8-bit usigned integer type."""

    def __init__(self, value: Any) -> None:  # noqa: D107
        # TODO: An assertion on dataype.
        super().__init__(value)


class UInt16Validator(_IntegralTypeValidator):
    """Eager validator implementation for 16-bit usigned integer type."""

    def __init__(self, value: Any) -> None:  # noqa: D107
        # TODO: An assertion on dataype.
        super().__init__(value)


class UInt32Validator(_IntegralTypeValidator):
    """Eager validator implementation for 32-bit usigned integer type."""

    def __init__(self, value: Any) -> None:  # noqa: D107
        # TODO: An assertion on dataype.
        super().__init__(value)


class UInt64Validator(_IntegralTypeValidator):
    """Eager validator implementation for 64-bit usigned integer type."""

    def __init__(self, value: Any) -> None:  # noqa: D107
        # TODO: An assertion on dataype.
        super().__init__(value)


class Float32Validator(_FractionalTypeValidator):
    """Eager validator implementation for 32-bit floating point type."""

    def __init__(self, value: Any) -> None:  # noqa: D107
        # TODO: An assertion on dataype.
        super().__init__(value)


class Float64Validator(_FractionalTypeValidator):
    """Eager validator implementation for 64-bit floating point type."""

    def __init__(self, value: Any) -> None:  # noqa: D107
        # TODO: An assertion on dataype.
        super().__init__(value)
