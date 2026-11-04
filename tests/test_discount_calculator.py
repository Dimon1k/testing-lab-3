import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from src.discount_calculator import DiscountCalculator

# Завантажуємо сценарії для DiscountCalculator
scenarios("../features/discount_calculator.feature")


@given("system is ready to calculate discount")
def system_ready():
    pass


@when(
    parsers.re(
        r"система обчислює ціну зі знижкою (?P<price>-?\d+(?:\.\d+)?),\s*(?P<discount>-?\d+(?:\.\d+)?)"
    ),
    target_fixture="calculation_result",
)
def calculate_discount(price, discount):
    calculator = DiscountCalculator()
    try:
        # Конвертуємо розпарсені рядки у float
        p = float(price)
        d = float(discount)
        result = calculator.calculate_discounted_price(p, d)
        return {"price": result, "error": None}
    except (TypeError, ValueError) as error:
        return {"price": None, "error": error}


@then(parsers.parse("підсумкова ціна повинна дорівнювати {expected:f}"))
def check_discounted_price(calculation_result, expected):
    assert calculation_result["error"] is None
    assert calculation_result["price"] == pytest.approx(expected)


@then(
    parsers.parse('система розрахунку повинна повернути помилку "{expected_message}"')
)
def check_discount_error(calculation_result, expected_message):
    assert calculation_result["error"] is not None
    assert str(calculation_result["error"]) == expected_message
