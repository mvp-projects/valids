"""Test numeric related validators."""
from typing import Type, Union

import pytest

from valids.exceptions import ValueValidationError
from valids.validators.numeric import (
    Int8TypeValidator,
    Int16TypeValidator,
    Int32TypeValidator,
    Int64TypeValidator,
    IntegralTypeValidator,
    NumericTypeValidator,
    UInt8TypeValidator,
    UInt16TypeValidator,
    UInt32TypeValidator,
    UInt64TypeValidator,
)


class TestInt8TypeValidator:
    """Test related to signed 8-bit signed integer type."""

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            -128,
            127,
        ],
    )
    def test_constructor_pass(self, value: int) -> None:
        """Test construction of value type passes."""
        Int8TypeValidator(value=value)

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            -128 - 1,
            127 + 1,
        ],
    )
    def test_constructor_fail(self, value: int) -> None:
        """Test construction of value type fails."""
        with pytest.raises(ValueValidationError):
            Int8TypeValidator(value=value)


class TestUInt8TypeValidator:
    """Test related to signed 8-bit unsigned integer type."""

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            0,
            255,
        ],
    )
    def test_constructor_pass(self, value: int) -> None:
        """Test construction of value type passes."""
        UInt8TypeValidator(value=value)

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            255 + 1,
        ],
    )
    def test_constructor_fail(self, value: int) -> None:
        """Test construction of value type fails."""
        with pytest.raises(ValueValidationError):
            UInt8TypeValidator(value=value)


class TestInt16TypeValidator:
    """Test related to signed 16-bit signed integer type."""

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            -32_768,
            32_767,
        ],
    )
    def test_constructor_pass(self, value: int) -> None:
        """Test construction of value type passes."""
        Int16TypeValidator(value=value)

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            -32_768 - 1,
            32_767 + 1,
        ],
    )
    def test_constructor_fail(self, value: int) -> None:
        """Test construction of value type fails."""
        with pytest.raises(ValueValidationError):
            Int16TypeValidator(value=value)


class TestUInt16TypeValidator:
    """Test related to signed 16-bit unsigned integer type."""

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            0,
            65_535,
        ],
    )
    def test_constructor_pass(self, value: int) -> None:
        """Test construction of value type passes."""
        UInt16TypeValidator(value=value)

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            65_535 + 1,
        ],
    )
    def test_constructor_fail(self, value: int) -> None:
        """Test construction of value type fails."""
        with pytest.raises(ValueValidationError):
            UInt16TypeValidator(value=value)


class TestInt32TypeValidator:
    """Test related to signed 32-bit signed integer type."""

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            -2_147_483_648,
            2_147_483_647,
        ],
    )
    def test_constructor_pass(self, value: int) -> None:
        """Test construction of value type passes."""
        Int32TypeValidator(value=value)

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            -2_147_483_648 - 1,
            2_147_483_647 + 1,
        ],
    )
    def test_constructor_fail(self, value: int) -> None:
        """Test construction of value type fails."""
        with pytest.raises(ValueValidationError):
            Int32TypeValidator(value=value)


class TestUInt32TypeValidator:
    """Test related to signed 32-bit unsigned integer type."""

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            0,
            4_294_967_295,
        ],
    )
    def test_constructor_pass(self, value: int) -> None:
        """Test construction of value type passes."""
        UInt32TypeValidator(value=value)

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            4_294_967_295 + 1,
        ],
    )
    def test_constructor_fail(self, value: int) -> None:
        """Test construction of value type fails."""
        with pytest.raises(ValueValidationError):
            UInt32TypeValidator(value=value)


class TestInt64TypeValidator:
    """Test related to signed 64-bit signed integer type."""

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            -9_223_372_036_854_775_808,
            9_223_372_036_854_775_807,
        ],
    )
    def test_constructor_pass(self, value: int) -> None:
        """Test construction of value type passes."""
        Int64TypeValidator(value=value)

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            -9_223_372_036_854_775_808 - 1,
            9_223_372_036_854_775_807 + 1,
        ],
    )
    def test_constructor_fail(self, value: int) -> None:
        """Test construction of value type fails."""
        with pytest.raises(ValueValidationError):
            Int64TypeValidator(value=value)


class TestUInt64TypeValidator:
    """Test related to signed 64-bit unsigned integer type."""

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            0,
            18_446_744_073_709_551_615,
        ],
    )
    def test_constructor_pass(self, value: int) -> None:
        """Test construction of value type passes."""
        UInt64TypeValidator(value=value)

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            18_446_744_073_709_551_615 + 1,
        ],
    )
    def test_constructor_fail(self, value: int) -> None:
        """Test construction of value type fails."""
        with pytest.raises(ValueValidationError):
            UInt64TypeValidator(value=value)


@pytest.mark.parametrize(
    argnames="numeric_type_validator",
    argvalues=[
        Int8TypeValidator,
        Int16TypeValidator,
        Int32TypeValidator,
        Int64TypeValidator,
    ],
)
class TestNumericTypeValidator:
    """Test related to all numeric types."""

    @pytest.mark.parametrize(
        argnames=["number", "gt"],
        argvalues=[
            (10, 3),
        ],
    )
    def test_greater_than_pass(
        self,
        numeric_type_validator: Type[NumericTypeValidator],
        number: Union[float, int],
        gt: Union[float, int],
    ) -> None:
        """Test greater_than works as expected."""
        numeric_type_validator(value=number).greater_than(other=gt)

    @pytest.mark.parametrize(
        argnames=["number", "gt"],
        argvalues=[
            (10, 30),
            (30, 30),
        ],
    )
    def test_greater_than_fail(
        self,
        numeric_type_validator: Type[NumericTypeValidator],
        number: Union[float, int],
        gt: Union[float, int],
    ) -> None:
        """Test greater_than fails as expected."""
        with pytest.raises(ValueValidationError):
            numeric_type_validator(value=number).greater_than(other=gt)

    @pytest.mark.parametrize(
        argnames=["number", "get"],
        argvalues=[
            (30, 10),
            (30, 30),
        ],
    )
    def test_greater_equal_than_pass(
        self,
        numeric_type_validator: Type[NumericTypeValidator],
        number: Union[float, int],
        get: Union[float, int],
    ) -> None:
        """Test greater_equal_than works as expected."""
        numeric_type_validator(value=number).greater_equal_than(other=get)

    @pytest.mark.parametrize(
        argnames=["number", "get"],
        argvalues=[
            (10, 30),
        ],
    )
    def test_greater_equal_than_fail(
        self,
        numeric_type_validator: Type[NumericTypeValidator],
        number: Union[float, int],
        get: Union[float, int],
    ) -> None:
        """Test greater_equal_than fails as expected."""
        with pytest.raises(ValueValidationError):
            numeric_type_validator(value=number).greater_equal_than(other=get)

    @pytest.mark.parametrize(
        argnames=["number", "lt"],
        argvalues=[
            (1, 3),
        ],
    )
    def test_less_than_pass(
        self,
        numeric_type_validator: Type[NumericTypeValidator],
        number: Union[float, int],
        lt: Union[float, int],
    ) -> None:
        """Test less_than works as expected."""
        numeric_type_validator(value=number).less_than(other=lt)

    @pytest.mark.parametrize(
        argnames=["number", "lt"],
        argvalues=[
            (100, 30),
            (30, 30),
        ],
    )
    def test_less_than_fail(
        self,
        numeric_type_validator: Type[NumericTypeValidator],
        number: Union[float, int],
        lt: Union[float, int],
    ) -> None:
        """Test less_than fails as expected."""
        with pytest.raises(ValueValidationError):
            numeric_type_validator(value=number).less_than(other=lt)

    @pytest.mark.parametrize(
        argnames=["number", "let"],
        argvalues=[
            (1, 3),
            (3, 3),
        ],
    )
    def test_less_equal_than_pass(
        self,
        numeric_type_validator: Type[NumericTypeValidator],
        number: Union[float, int],
        let: Union[float, int],
    ) -> None:
        """Test less_equal_than works as expected."""
        numeric_type_validator(value=number).less_equal_than(other=let)

    @pytest.mark.parametrize(
        argnames=["number", "let"],
        argvalues=[
            (100, 30),
        ],
    )
    def test_less_equal_than_fail(
        self,
        numeric_type_validator: Type[NumericTypeValidator],
        number: Union[float, int],
        let: Union[float, int],
    ) -> None:
        """Test less_equal_than fails as expected."""
        with pytest.raises(ValueValidationError):
            numeric_type_validator(value=number).less_equal_than(other=let)


@pytest.mark.parametrize(
    argnames="integral_type_validator",
    argvalues=[
        Int8TypeValidator,
        Int16TypeValidator,
        Int32TypeValidator,
        Int64TypeValidator,
    ],
)
class TestIntegralTypeValidator:
    """Test related to all integral types."""

    @pytest.mark.parametrize(
        argnames=["number", "multiple_of"],
        argvalues=[
            (3, 3),
            (3, 1),
            (18, 2),
        ],
    )
    def test_multiple_of_pass(
        self,
        integral_type_validator: Type[IntegralTypeValidator],
        number: int,
        multiple_of: int,
    ) -> None:
        """Test multiple_of works as expected."""
        integral_type_validator(value=number).multiple_of(of=multiple_of)

    @pytest.mark.parametrize(
        argnames=["number", "multiple_of"],
        argvalues=[
            (3, 2),
            (18, 5),
        ],
    )
    def test_multiple_of_fail(
        self,
        integral_type_validator: Type[IntegralTypeValidator],
        number: int,
        multiple_of: int,
    ) -> None:
        """Test multiple_of fails as expected."""
        with pytest.raises(ValueValidationError):
            integral_type_validator(value=number).multiple_of(of=multiple_of)

    @pytest.mark.parametrize(
        argnames=["number", "other"],
        argvalues=[
            (3, 3),
        ],
    )
    def test_equal_pass(
        self,
        integral_type_validator: Type[IntegralTypeValidator],
        number: int,
        other: int,
    ) -> None:
        """Test equal works as expected."""
        integral_type_validator(value=number).equal(other=other)

    @pytest.mark.parametrize(
        argnames=["number", "other"],
        argvalues=[
            (3, 2),
        ],
    )
    def test_equal_fail(
        self,
        integral_type_validator: Type[IntegralTypeValidator],
        number: int,
        other: int,
    ) -> None:
        """Test equal fails as expected."""
        with pytest.raises(ValueValidationError):
            integral_type_validator(value=number).equal(other=other)
