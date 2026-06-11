import pytest

from unit_converter.registry import UnitRegistry


@pytest.fixture
def registry() -> UnitRegistry:
    return UnitRegistry.default()
