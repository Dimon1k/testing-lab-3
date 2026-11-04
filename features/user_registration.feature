Feature: User Registration Validation
  As a user registration system
  I want to validate user credentials
  So that only valid registration data is accepted

  Scenario: Registration with invalid email
    Given system is ready to validate user
    When система перевіряє реєстраційні дані "invalid-email", "Password123", 25
    Then система повинна відхилити дані з помилкою "Email is invalid"

  Scenario: Registration with short password
    Given system is ready to validate user
    When система перевіряє реєстраційні дані "user@example.com", "pass1", 25
    Then система повинна відхилити дані з помилкою "Password must contain at least 8 characters"

  Scenario: Registration with password without digits
    Given system is ready to validate user
    When система перевіряє реєстраційні дані "user@example.com", "Password", 25
    Then система повинна відхилити дані з помилкою "Password must contain a digit"

  Scenario: Registration with underage age
    Given system is ready to validate user
    When система перевіряє реєстраційні дані "user@example.com", "Password123", 17
    Then система повинна відхилити дані з помилкою "Age must be between 18 and 120"
