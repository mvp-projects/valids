"""Boolean related validators."""
from typing import final

from typing_extensions import Self

from valids.base import IValidator
from valids.exceptions import ValueValidationError


@final
class BooleanTypeValidator(IValidator):
    """Validator implementation for boolean values."""

    def __init__(self, value: bool) -> None:  # noqa: D107, FBT001
        self.value = value

    @final
    def is_true(self) -> Self:
        """Check if boolean value is True."""
        if self.value:
            return self
        raise ValueValidationError(msg=f"{self.value} is not true.")

    @final
    def is_false(self) -> Self:
        """Check if boolean value is False."""
        if not self.value:
            return self
        raise ValueValidationError(msg=f"{self.value} is not false.")
