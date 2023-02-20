"""Test boolean related validator."""
import pytest

from valids.exceptions import ValueValidationError
from valids.validators.boolean import BooleanTypeValidator


class TestBooleanValidator:
    """Test related to boolean values."""

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[True, False],
    )
    def test_constructor_pass(self, value: bool) -> None:  # noqa: FBT001
        """Test construction of value type passes."""
        BooleanTypeValidator(value=value)

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[True],
    )
    def test_is_true_pass(self, value: bool) -> None:  # noqa: FBT001
        """Test is_true works as expected."""
        BooleanTypeValidator(value=value).is_true()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[False],
    )
    def test_is_true_fails(self, value: bool) -> None:  # noqa: FBT001
        """Test is_true works as expected."""
        with pytest.raises(ValueValidationError):
            BooleanTypeValidator(value=value).is_true()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[False],
    )
    def test_is_false_pass(self, value: bool) -> None:  # noqa: FBT001
        """Test is_false works as expected."""
        BooleanTypeValidator(value=value).is_false()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[True],
    )
    def test_is_false_fails(self, value: bool) -> None:  # noqa: FBT001
        """Test is_false works as expected."""
        with pytest.raises(ValueValidationError):
            BooleanTypeValidator(value=value).is_false()
