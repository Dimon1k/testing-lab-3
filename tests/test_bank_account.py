import pytest

from src.bank_account import BankAccount


def test_initial_balance_default():
    """Створення рахунку без аргументів (баланс має бути 0)"""
    account = BankAccount()
    assert account.balance == 0


def test_initial_balance_custom():
    """Створення рахунку з початковим балансом (наприклад, 250)"""
    account = BankAccount(250)
    assert account.balance == 250


def test_negative_initial_balance():
    """Перевірка на від'ємний початковий баланс"""
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount(-100)


def test_deposit_positive_amount():
    """Поповнення позитивною сумою"""
    account = BankAccount(100)
    account.deposit(50)
    assert account.balance == 150


def test_deposit_zero_or_negative():
    """Спроба поповнення на 0 або від'ємну суму"""
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.deposit(0)
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.deposit(-50)


def test_withdraw_successful():
    """Успішне зняття коштів"""
    account = BankAccount(100)
    account.withdraw(40)
    assert account.balance == 60


def test_withdraw_zero_or_negative():
    """Спроба зняття 0 або від'ємної суми"""
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.withdraw(0)
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.withdraw(-20)


def test_withdraw_insufficient_funds():
    """Спроба зняти більше грошей, ніж є на рахунку"""
    account = BankAccount(50)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(100)
