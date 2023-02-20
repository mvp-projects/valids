"""Test utf-8 encoded string related validator."""

import re

import pytest

from valids.exceptions import ValueValidationError
from valids.validators.string import Utf8TypeValidator


class TestUtf8TypeValidator:
    """Test related to utf-8 encoded string values."""

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            "name",
            "last_name",
        ],
    )
    def test_constructor_pass(self, value: str) -> None:
        """Test construction of value type passes."""
        Utf8TypeValidator(value=value)

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=["ab123"],
    )
    def test_is_alnum_pass(self, value: str) -> None:
        """Test is_alnum works as expected."""
        Utf8TypeValidator(value=value).is_alnum()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=["ab123#"],
    )
    def test_is_alnum_fails(self, value: str) -> None:
        """Test is_alnum works as expected."""
        with pytest.raises(ValueValidationError):
            Utf8TypeValidator(value=value).is_alnum()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=["abcABC"],
    )
    def test_is_alpha_pass(self, value: str) -> None:
        """Test is_alpha works as expected."""
        Utf8TypeValidator(value=value).is_alpha()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=["abcABC123"],
    )
    def test_is_alpha_fails(self, value: str) -> None:
        """Test is_alpha works as expected."""
        with pytest.raises(ValueValidationError):
            Utf8TypeValidator(value=value).is_alpha()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=["123"],
    )
    def test_is_digit_pass(self, value: str) -> None:
        """Test is_digit works as expected."""
        Utf8TypeValidator(value=value).is_digit()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=["1233a"],
    )
    def test_is_digit_fails(self, value: str) -> None:
        """Test is_digit works as expected."""
        with pytest.raises(ValueValidationError):
            Utf8TypeValidator(value=value).is_digit()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=["i_am_lower"],
    )
    def test_is_lower_pass(self, value: str) -> None:
        """Test is_lower works as expected."""
        Utf8TypeValidator(value=value).is_lower()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=["i_am_NOT_lower"],
    )
    def test_is_lower_fails(self, value: str) -> None:
        """Test is_lower works as expected."""
        with pytest.raises(ValueValidationError):
            Utf8TypeValidator(value=value).is_lower()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=["I_AM_UPPER"],
    )
    def test_is_upper_pass(self, value: str) -> None:
        """Test is_upper works as expected."""
        Utf8TypeValidator(value=value).is_upper()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=["I_AM_not_UPPER"],
    )
    def test_is_upper_fails(self, value: str) -> None:
        """Test is_upper works as expected."""
        with pytest.raises(ValueValidationError):
            Utf8TypeValidator(value=value).is_upper()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[" "],
    )
    def test_is_space_pass(self, value: str) -> None:
        """Test is_space works as expected."""
        Utf8TypeValidator(value=value).is_space()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            "",
            "abc",
            "123",
        ],
    )
    def test_is_space_fails(self, value: str) -> None:
        """Test is_space works as expected."""
        with pytest.raises(ValueValidationError):
            Utf8TypeValidator(value=value).is_space()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=["A Title Well Written"],
    )
    def test_is_title_pass(self, value: str) -> None:
        """Test is_title works as expected."""
        Utf8TypeValidator(value=value).is_title()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=["A title not well written"],
    )
    def test_is_title_fails(self, value: str) -> None:
        """Test is_title works as expected."""
        with pytest.raises(ValueValidationError):
            Utf8TypeValidator(value=value).is_title()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=["A Title Well Written"],
    )
    def test_is_ascii_pass(self, value: str) -> None:
        """Test is_ascii works as expected."""
        Utf8TypeValidator(value=value).is_ascii()

    @pytest.mark.parametrize(
        argnames="value",
        argvalues=[
            "日本人 中國的 ~=[]()%+{}@;",
            "[\x80-\xFF]",
        ],
    )
    def test_is_ascii_fails(self, value: str) -> None:
        """Test is_ascii works as expected."""
        with pytest.raises(ValueValidationError):
            Utf8TypeValidator(value=value).is_ascii()

    @pytest.mark.parametrize(
        argnames=[
            "value",
            "suffix",
        ],
        argvalues=[
            (
                "A Title Well Written",
                "en",
            )
        ],
    )
    def test_endswith_pass(
        self,
        value: str,
        suffix: str,
    ) -> None:
        """Test endswith works as expected."""
        Utf8TypeValidator(value=value).endswith(suffix=suffix)

    @pytest.mark.parametrize(
        argnames=[
            "value",
            "suffix",
        ],
        argvalues=[
            (
                "A Title Well Written",
                "not en",
            )
        ],
    )
    def test_endswith_fails(
        self,
        value: str,
        suffix: str,
    ) -> None:
        """Test endswith works as expected."""
        with pytest.raises(ValueValidationError):
            Utf8TypeValidator(value=value).endswith(suffix=suffix)

    @pytest.mark.parametrize(
        argnames=[
            "value",
            "prefix",
        ],
        argvalues=[
            (
                "A Title Well Written",
                "A T",
            )
        ],
    )
    def test_startswith_pass(
        self,
        value: str,
        prefix: str,
    ) -> None:
        """Test startswith works as expected."""
        Utf8TypeValidator(value=value).startswith(prefix=prefix)

    @pytest.mark.parametrize(
        argnames=[
            "value",
            "prefix",
        ],
        argvalues=[
            (
                "A Title Well Written",
                "Not A Title",
            )
        ],
    )
    def test_startswith_fails(
        self,
        value: str,
        prefix: str,
    ) -> None:
        """Test startswith works as expected."""
        with pytest.raises(ValueValidationError):
            Utf8TypeValidator(value=value).startswith(prefix=prefix)

    @pytest.mark.parametrize(
        argnames=[
            "value",
            "pattern",
        ],
        argvalues=[
            (
                "aaaaaa",
                re.compile(pattern=r"a+"),
            ),
            (
                "abcde",
                re.compile(pattern=r"[a-z]+"),
            ),
            (
                "ABCDE",
                re.compile(pattern=r"[A-Z]+"),
            ),
            (
                "abcABC",
                re.compile(pattern=r"[a-zA-Z]+"),
            ),
            (
                "123abcABCZZZzzz888",
                re.compile(pattern=r"[0-9a-zA-Z]+"),
            ),
        ],
    )
    def test_match_regex_pass(
        self,
        value: str,
        pattern: re.Pattern[str],
    ) -> None:
        """Test match_regex works as expected."""
        Utf8TypeValidator(value=value).match_regex(pattern=pattern)

    @pytest.mark.parametrize(
        argnames=[
            "value",
            "pattern",
        ],
        argvalues=[
            (
                "aaaabaa",
                re.compile(pattern=r"a+"),
            ),
            (
                "abcdeZ",
                re.compile(pattern=r"[a-z]+"),
            ),
            (
                "ABCDEa",
                re.compile(pattern=r"[A-Z]+"),
            ),
            (
                "abcABC123",
                re.compile(pattern=r"[a-zA-Z]+"),
            ),
            (
                "123abcABCZZZzzz888@",
                re.compile(pattern=r"[0-9a-zA-Z]+"),
            ),
        ],
    )
    def test_match_regex_fails(
        self,
        value: str,
        pattern: re.Pattern[str],
    ) -> None:
        """Test match_regex works as expected."""
        with pytest.raises(ValueValidationError):
            Utf8TypeValidator(value=value).match_regex(pattern=pattern)
