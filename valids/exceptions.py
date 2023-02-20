"""Custom errors."""


class ValueValidationError(Exception):
    """Error raised when valua validation fails."""

    def __init__(self, msg: str) -> None:
        """Construct error."""
        super().__init__(msg)
