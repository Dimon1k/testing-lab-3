import pytest

from src.temperature_converter import TemperatureConverter

# --- Перетворення температури (Success Cases) ---


def test_celsius_to_fahrenheit_boiling():
    """100 °C -> 212 °F"""
    result = TemperatureConverter.celsius_to_fahrenheit(100)
    assert result == pytest.approx(212.0)


def test_fahrenheit_to_celsius_freezing():
    """32 °F -> 0 °C"""
    result = TemperatureConverter.fahrenheit_to_celsius(32)
    assert result == pytest.approx(0.0)


def test_fahrenheit_to_celsius_boiling():
    """212 °F -> 100 °C"""
    result = TemperatureConverter.fahrenheit_to_celsius(212)
    assert result == pytest.approx(100.0)


# --- Перевірка винятків (Edge Cases & Validation) ---


def test_invalid_type_raises_type_error():
    """Рядок замість числа -> TypeError"""
    with pytest.raises(TypeError, match="Value must be a number"):
        TemperatureConverter.celsius_to_fahrenheit("100")

    with pytest.raises(TypeError, match="Value must be a number"):
        TemperatureConverter.fahrenheit_to_celsius("212")


def test_celsius_below_absolute_zero_raises_value_error():
    """Значення нижче -273.15 °C -> ValueError"""
    with pytest.raises(ValueError, match="Temperature cannot be below absolute zero"):
        TemperatureConverter.celsius_to_fahrenheit(-274.0)


def test_fahrenheit_below_absolute_zero_raises_value_error():
    """Значення нижче -459.67 °F -> ValueError"""
    with pytest.raises(ValueError, match="Temperature cannot be below absolute zero"):
        TemperatureConverter.fahrenheit_to_celsius(-460.0)
