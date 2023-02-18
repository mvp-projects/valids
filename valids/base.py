"""Interface and abstract class definitions."""

import abc
from typing import Any


class IValidator(abc.ABC):
    """Interface for data validators types."""

    @abc.abstractmethod
    def __init__(self, value: Any) -> None:  # noqa: D107
        raise NotImplementedError()
