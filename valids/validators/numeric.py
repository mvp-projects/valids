"""Numeric related validators."""

import abc
from typing import Tuple, Union, final

from typing_extensions import Self

from valids.base import IValidator
from valids.exceptions import ValueValidationError


class NumericTypeValidator(IValidator, abc.ABC):
    """Validator base class for numeric values."""

    def __init__(self, value: Union[float, int]) -> None:  # noqa: D107
        self.value = value


class IntegralTypeValidator(NumericTypeValidator, abc.ABC):
    """Validator base class for integral data types."""

    def __init__(self, value: int) -> None:  # noqa: D107
        super().__init__(value)

    @final
    def _check_for_bits(self, value: int, expected_bits: int) -> bool:
        return value.bit_length() <= expected_bits

    @final
    def _check_range(self, value: int, expected_range: Tuple[int, int]) -> bool:
        return expected_range[0] <= value <= expected_range[1]

    @final
    def multiple_of(self, of: int) -> Self:
        """Check integer value is multiple of other value."""
        if self.value % of == 0:
            return self
        raise ValueValidationError(
            msg=f"{self.value} is not a multiple of {of}",
        )

    @final
    def equal(self, other: float) -> Self:
        """Check numeric value is equal to other value."""
        if self.value == other:
            return self
        raise ValueValidationError(
            msg=f"{self.value} is not a equal to {other}",
        )

    @final
    def greater_than(self, other: int) -> Self:
        """Check numeric value is greater than other value."""
        if self.value > other:
            return self
        raise ValueValidationError(
            msg=f"{self.value} is not greater than {other}",
        )

    @final
    def greater_equal_than(self, other: int) -> Self:
        """Check numeric value is greater or equal than other value."""
        if self.value >= other:
            return self
        raise ValueValidationError(
            msg=f"{self.value} is not greater or equal than {other}",
        )

    @final
    def less_than(self, other: int) -> Self:
        """Check numeric value is less than other value."""
        if self.value < other:
            return self
        raise ValueValidationError(
            msg=f"{self.value} is not less than {other}",
        )

    @final
    def less_equal_than(self, other: int) -> Self:
        """Check numeric value is less or equal than other value."""
        if self.value <= other:
            return self
        raise ValueValidationError(
            msg=f"{self.value} is not less or equal than {other}",
        )


class _FractionalTypeValidator(NumericTypeValidator):
    """Validator base class for fractional data types."""


@final
class Int8TypeValidator(IntegralTypeValidator):
    """Validator implementation for 8-bit signed integer type."""

    def __init__(self, value: int) -> None:  # noqa: D107
        bounds = (-128, 127)
        n_bit = 8
        if not (
            self._check_for_bits(value=value, expected_bits=n_bit)
            and self._check_range(value=value, expected_range=bounds)
        ):
            raise ValueValidationError(msg=f"{value} is not an 8-bit signed integer.")
        super().__init__(value)


@final
class Int16TypeValidator(IntegralTypeValidator):
    """Validator implementation for 16-bit signed integer type."""

    def __init__(self, value: int) -> None:  # noqa: D107
        bounds = (-32_768, 32_767)
        n_bit = 16
        if not (
            self._check_for_bits(value=value, expected_bits=n_bit)
            and self._check_range(value=value, expected_range=bounds)
        ):
            raise ValueValidationError(msg=f"{value} is not an 16-bit signed integer.")
        super().__init__(value)


@final
class Int32TypeValidator(IntegralTypeValidator):
    """Validator implementation for 32-bit signed integer type."""

    def __init__(self, value: int) -> None:  # noqa: D107
        bounds = (-2_147_483_648, 2_147_483_647)
        n_bit = 32
        if not (
            self._check_for_bits(value=value, expected_bits=n_bit)
            and self._check_range(value=value, expected_range=bounds)
        ):
            raise ValueValidationError(msg=f"{value} is not an 16-bit signed integer.")
        super().__init__(value)


@final
class Int64TypeValidator(IntegralTypeValidator):
    """Validator implementation for 64-bit signed integer type."""

    def __init__(self, value: int) -> None:  # noqa: D107
        bounds = (-9_223_372_036_854_775_808, 9_223_372_036_854_775_807)
        n_bit = 64
        if not (
            self._check_for_bits(value=value, expected_bits=n_bit)
            and self._check_range(value=value, expected_range=bounds)
        ):
            raise ValueValidationError(msg=f"{value} is not an 16-bit signed integer.")
        super().__init__(value)


@final
class UInt8TypeValidator(IntegralTypeValidator):
    """Validator implementation for 8-bit usigned integer type."""

    def __init__(self, value: int) -> None:  # noqa: D107
        bounds = (0, 255)
        n_bit = 8
        if not (
            self._check_for_bits(value=value, expected_bits=n_bit)
            and self._check_range(value=value, expected_range=bounds)
        ):
            raise ValueValidationError(msg=f"{value} is not an 8-bit unsigned integer.")
        super().__init__(value)


@final
class UInt16TypeValidator(IntegralTypeValidator):
    """Validator implementation for 16-bit usigned integer type."""

    def __init__(self, value: int) -> None:  # noqa: D107
        bounds = (0, 65_535)
        n_bit = 16
        if not (
            self._check_for_bits(value=value, expected_bits=n_bit)
            and self._check_range(value=value, expected_range=bounds)
        ):
            raise ValueValidationError(
                msg=f"{value} is not an 16-bit unsigned integer."
            )
        super().__init__(value)


@final
class UInt32TypeValidator(IntegralTypeValidator):
    """Validator implementation for 32-bit usigned integer type."""

    def __init__(self, value: int) -> None:  # noqa: D107
        bounds = (0, 4_294_967_295)
        n_bit = 32
        if not (
            self._check_for_bits(value=value, expected_bits=n_bit)
            and self._check_range(value=value, expected_range=bounds)
        ):
            raise ValueValidationError(
                msg=f"{value} is not an 32-bit unsigned integer."
            )
        super().__init__(value)


@final
class UInt64TypeValidator(IntegralTypeValidator):
    """Validator implementation for 64-bit usigned integer type."""

    def __init__(self, value: int) -> None:  # noqa: D107
        bounds = (0, 18_446_744_073_709_551_615)
        n_bit = 64
        if not (
            self._check_for_bits(value=value, expected_bits=n_bit)
            and self._check_range(value=value, expected_range=bounds)
        ):
            raise ValueValidationError(
                msg=f"{value} is not an 64-bit unsigned integer."
            )
        super().__init__(value)


@final
class Float32TypeValidator(_FractionalTypeValidator):
    """Validator implementation for 32-bit floating point type."""

    def __init__(self, value: float) -> None:  # noqa: D107
        # TODO: An assertion on dataype.
        super().__init__(value)


@final
class Float64TypeValidator(_FractionalTypeValidator):
    """Validator implementation for 64-bit floating point type."""

    def __init__(self, value: float) -> None:  # noqa: D107
        # TODO: An assertion on dataype.
        super().__init__(value)
