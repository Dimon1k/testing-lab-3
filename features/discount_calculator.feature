Feature: Discount Calculator Validation
  As a store system
  I want to calculate discounted prices and validate input
  So that invalid prices or discounts are rejected

  Scenario: Calculate standard discount
    Given system is ready to calculate discount
    When система обчислює ціну зі знижкою 100, 20
    Then підсумкова ціна повинна дорівнювати 80.0

  Scenario: Discount 0 percent
    Given system is ready to calculate discount
    When система обчислює ціну зі знижкою 100, 0
    Then підсумкова ціна повинна дорівнювати 100.0

  Scenario: Discount 100 percent
    Given system is ready to calculate discount
    When система обчислює ціну зі знижкою 100, 100
    Then підсумкова ціна повинна дорівнювати 0.0

  Scenario: Negative price raises ValueError
    Given system is ready to calculate discount
    When система обчислює ціну зі знижкою -50, 10
    Then система розрахунку повинна повернути помилку "Price cannot be negative"

  Scenario: Discount 101 percent raises ValueError
    Given system is ready to calculate discount
    When система обчислює ціну зі знижкою 100, 101
    Then система розрахунку повинна повернути помилку "Discount percent must be between 0 and 100"
