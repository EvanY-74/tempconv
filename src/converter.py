# Absolute zero in Celsius
ABSOLUTE_ZERO_C = -273.15


def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit
    """
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius
    """
    return (f - 32) * 5/9
    ...


def celsius_to_kelvin(c: float) -> float:
    """Convert Celsius to Kelvin
    """
    if c < ABSOLUTE_ZERO_C:
        raise ValueError(
            f"Celsius value cannot be below absolute zero ({ABSOLUTE_ZERO_C})"
        )
    return c - ABSOLUTE_ZERO_C


def kelvin_to_celsius(k: float) -> float:
    """Convert Kelvin to Celsius
    """
    if k < 0:
        raise ValueError("Kelvin value cannot be below absolute zero")
    return k + ABSOLUTE_ZERO_C


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a temperature between F, C, and K
    """
    # Normalize to uppercase so 'c' and 'C' both work
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    # If same unit, do nothing
    if from_unit == to_unit:
        return float(value)

    # C → F, C → K, F → C, F → K (through C), K → C, K → F (through C)
    if from_unit == 'C':
        if to_unit == 'F':
            return celsius_to_fahrenheit(value)
        elif to_unit == 'K':
            return celsius_to_kelvin(value)
    elif from_unit == 'F':
        if to_unit == 'C':
            return fahrenheit_to_celsius(value)
        elif to_unit == 'K':
            return celsius_to_kelvin(fahrenheit_to_celsius(value))
    elif from_unit == 'K':
        if to_unit == 'C':
            return kelvin_to_celsius(value)
        elif to_unit == 'F':
            return celsius_to_fahrenheit(kelvin_to_celsius(value))

    raise ValueError("At least one unit is not recognized")
