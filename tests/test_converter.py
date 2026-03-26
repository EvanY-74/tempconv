import pytest
from src.converter import celsius_to_fahrenheit, celsius_to_kelvin, kelvin_to_celsius, convert, ABSOLUTE_ZERO_C

# ── Basic tests using fixtures ──────────────────────────────────

def test_freezing_c_to_f(freezing_point):
    # freezing_point is injected from conftest.py
    assert celsius_to_fahrenheit(freezing_point["C"]) == freezing_point["F"]

def test_boiling_c_to_f(boiling_point):
    assert celsius_to_fahrenheit(boiling_point["C"]) == boiling_point["F"]

# ── Parametrize for multiple conversion cases ───────────────────

@pytest.mark.parametrize("c, expected_f", [
    (0,    32.0),   # freezing
    (100,  212.0),  # boiling
    (-40,  -40.0),  # where C and F are equal
    (37,   98.6),   # body temperature
])
def test_c_to_f_cases(c, expected_f):
    assert celsius_to_fahrenheit(c) == pytest.approx(expected_f, rel=1e-3)

# ── Edge cases ──────────────────────────────────────────────────

@pytest.mark.edge
def test_absolute_zero_kelvin():
    assert celsius_to_kelvin(-273.15) == pytest.approx(0.0)


@pytest.mark.edge
def test_below_absolute_zero_c_raises():
    with pytest.raises(ValueError):
        celsius_to_kelvin(-300)

@pytest.mark.edge
def test_below_absolute_zero_k_raises():
    with pytest.raises(ValueError):
        kelvin_to_celsius(-0.1)

@pytest.mark.edge
def test_convert_same_unit():
    assert convert(25, 'C', 'c') == pytest.approx(25.0)


@pytest.mark.edge
def test_convert_with_invalid_unit_raises():
    with pytest.raises(ValueError):
        convert(30.0, 'C', 'X')


@pytest.mark.parametrize("value, from_unit, to_unit, expected_f", [
    (0, 'C', 'F', 32.0),
    (0, 'C', 'K', -ABSOLUTE_ZERO_C),
    (32.0, 'F', 'C', 0),
    (32.0, 'F', 'K', -ABSOLUTE_ZERO_C),
    (-ABSOLUTE_ZERO_C, 'K', 'C', 0),
    (-ABSOLUTE_ZERO_C, 'K', 'F', 32.0)
])
def test_all_convert_cases(value, from_unit, to_unit, expected_f):
    assert convert(value, from_unit, to_unit) == pytest.approx(expected_f, rel=1e-3)