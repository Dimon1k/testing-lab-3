class TemperatureConverter:
    ABSOLUTE_ZERO_CELSIUS = -273.15
    ABSOLUTE_ZERO_FAHRENHEIT = -459.67

    @staticmethod
    def celsius_to_fahrenheit(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value < TemperatureConverter.ABSOLUTE_ZERO_CELSIUS:
            raise ValueError(
                f"Temperature cannot be below absolute zero ({TemperatureConverter.ABSOLUTE_ZERO_CELSIUS} °C)"
            )
        return value * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value < TemperatureConverter.ABSOLUTE_ZERO_FAHRENHEIT:
            raise ValueError(
                f"Temperature cannot be below absolute zero ({TemperatureConverter.ABSOLUTE_ZERO_FAHRENHEIT} °F)"
            )
        return (value - 32) * 5 / 9
