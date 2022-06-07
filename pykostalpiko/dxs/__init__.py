"""Description of DxsEntries."""
from dataclasses import dataclass
from typing import Callable, Any


@dataclass
class Descriptor:
    """Data structure to describe a DxsEntry"""

    def __init__(
        self,
        key: int,
        name: str,
        unit: str = None,
        configurable: bool = False,
        mapper_function: Callable[[Any], Any] = None,
        multiplication_factor: float = 1,
    ) -> None:
        """Constructor."""
        self.key = key
        self.name = name
        self.unit = unit
        self._configurable = configurable
        self._mapper_function = mapper_function
        self._multiplication_factor = multiplication_factor


@dataclass
class ConfigurableDescriptor(Descriptor):
    def __init__(
        self,
        key: int,
        name: str,
        unit: str = None,
        mapper_function: Callable[[Any], Any] = None,
        multiplication_factor: float = 1,
    ) -> None:
        super().__init__(key, name, unit, True, mapper_function, multiplication_factor)


@dataclass
class Value:
    """Data structure to hold a DxsEntry key value pair."""

    def __init__(self, key: int, value: str | int | float) -> None:
        """Constructor."""
        self.key = key
        self.value = value


class MapperException(Exception):
    """Exception raised when a mapping is not found."""
