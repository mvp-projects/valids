"""Utf-8 related validators."""

import re
from typing import final

from typing_extensions import Self

from valids.base import IValidator
from valids.exceptions import ValueValidationError


@final
class Utf8TypeValidator(IValidator):
    """Validator implementation for utf-8 encoded string values."""

    def __init__(self, value: str) -> None:  # noqa: D107
        self.value = value

    def is_alnum(self) -> Self:
        """Check if utf-8 encoded string value is alpha-numeric."""
        if self.value.isalnum():
            return self
        raise ValueValidationError(
            f"{self.value} is not an alpha-numeric utf-8 encoded string"
        )

    def is_alpha(self) -> Self:
        """Check if utf-8 encoded string value is alphabetic."""
        if self.value.isalpha():
            return self
        raise ValueValidationError(
            f"{self.value} is not an alphabetic utf-8 encoded string"
        )

    def is_digit(self) -> Self:
        """Check if utf-8 encoded string value is digit."""
        if self.value.isdigit():
            return self
        raise ValueValidationError(f"{self.value} is not a digit utf-8 encoded string")

    def is_lower(self) -> Self:
        """Check if utf-8 encoded string value is lowercase."""
        if self.value.islower():
            return self
        raise ValueValidationError(
            f"{self.value} is not a lowercase utf-8 encoded string"
        )

    def is_upper(self) -> Self:
        """Check if utf-8 encoded string value is uppercase."""
        if self.value.isupper():
            return self
        raise ValueValidationError(
            f"{self.value} is not a uppercase utf-8 encoded string"
        )

    def is_space(self) -> Self:
        """Check if utf-8 encoded string value is a whitespace."""
        if self.value.isspace():
            return self
        raise ValueValidationError(f"{self.value} is not a whitespace")

    def is_title(self) -> Self:
        """Check if utf-8 encoded string value its title-cased."""
        if self.value.istitle():
            return self
        self.value.isascii
        raise ValueValidationError(f"{self.value} is not title-cased")

    def is_ascii(self) -> Self:
        """Check if all characters in utf-8 encoded string are ASCII."""
        if self.value.isascii():
            return self
        raise ValueValidationError(f"Not all characters in {self.value} are ASCII.")

    def endswith(self, suffix: str) -> Self:
        """Check if utf-8 encoded string value ends with a suffix."""
        if self.value.endswith(suffix):
            return self
        raise ValueValidationError(f"{self.value} does not ends with {suffix}")

    def startswith(self, prefix: str) -> Self:
        """Check if utf-8 encoded string value starts with a prefix."""
        if self.value.startswith(prefix):
            return self
        raise ValueValidationError(f"{self.value} does not starts with {prefix}")

    def match_regex(self, pattern: re.Pattern[str]) -> Self:
        """Check if utf-8 encoded string match an specified regex pattern."""
        match = pattern.fullmatch(string=self.value)
        if match:
            return self
        raise ValueValidationError(f"{self.value} does not match pattern {pattern}")
