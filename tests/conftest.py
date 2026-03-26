import pytest
from src.converter import ABSOLUTE_ZERO_C


@pytest.fixture
def freezing_point():
    """Returns the freezing point in all three units."""
    return {"C": 0.0, "F": 32.0, "K": -ABSOLUTE_ZERO_C}


@pytest.fixture
def boiling_point():
    """Returns the boiling point in all three units."""
    return {"C": 100.0, "F": 212.0, "K": -ABSOLUTE_ZERO_C + 100}
