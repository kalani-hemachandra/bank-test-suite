import unittest
from bank.app import BankAccount

class TestBankAccountIntegration(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount()

    def test_deposit_then_withdraw_within_limit(self):
        self.account.cash_deposit(500)
        self.assertEqual(self.account.cash_withdraw(300), 1200)
        self.assertEqual(self.account.balance, 1200)

    def test_deposit_then_withdraw_exceeding_limit(self):
        self.account.cash_deposit(200)
        self.assertEqual(self.account.cash_withdraw(400), 1200) # Should not allow
        self.assertEqual(self.account.balance, 1200)

    def test_deposit_then_interest_applied(self):
        self.account.cash_deposit(1000)
        initial_balance = self.account.balance
        rate = 3.5 / 12
        self.account.monthly_interest(rate)
        expected_balance = initial_balance + (initial_balance * rate) / 100
        self.assertAlmostEqual(self.account.balance, expected_balance, places=2)

    def test_withdraw_then_deposit(self):
        returned_balance_withdraw = self.account.cash_withdraw(200)
        self.assertEqual(returned_balance_withdraw, 1000)  # Withdrawal should be prevented
        self.assertEqual(self.account.balance, 1000)  # Balance should remain 1000
        self.account.cash_deposit(500)
        self.assertEqual(self.account.balance, 1500)

#    def test_withdraw_then_deposit(self):
#        self.account.cash_withdraw(200)
#        self.assertEqual(self.account.balance, 800)
#        self.account.cash_deposit(500)
#        self.assertEqual(self.account.balance, 1300)

    def test_interest_then_withdraw(self):
        initial_balance = self.account.balance
        rate = 3.5 / 12
        self.account.monthly_interest(rate)
        interest_earned = (initial_balance * rate) / 100
        # Try to withdraw an amount less than the interest earned
        withdraw_amount = interest_earned / 2
        self.account.cash_withdraw(withdraw_amount)
        expected_balance = initial_balance + interest_earned - withdraw_amount
        self.assertAlmostEqual(self.account.balance, expected_balance, places=2)

    def test_deposit_withdraw_deposit(self):
        self.account.cash_deposit(500)
        self.account.cash_withdraw(200)
        self.account.cash_deposit(300)
        self.assertEqual(self.account.balance, 1600)

    def test_withdraw_deposit_withdraw_near_limit(self):
        self.account.cash_deposit(1100) # Balance 2100
        self.account.cash_withdraw(1000) # Balance 1100
        self.assertEqual(self.account.cash_withdraw(99), 1001) # Should allow
        self.assertEqual(self.account.balance, 1001)