import unittest
from bank.app import BankAccount

class TestBankAccountUnit(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount()

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000)

    def test_cash_deposit_positive(self):
        initial_balance = self.account.balance
        deposit_amount = 500
        self.assertEqual(self.account.cash_deposit(deposit_amount), initial_balance + deposit_amount)
        self.assertEqual(self.account.balance, initial_balance + deposit_amount)

    def test_cash_deposit_negative(self):
        initial_balance = self.account.balance
        deposit_amount = -100
        self.assertEqual(self.account.cash_deposit(deposit_amount), initial_balance)
        self.assertEqual(self.account.balance, initial_balance)

    def test_cash_deposit_zero(self):
        initial_balance = self.account.balance
        deposit_amount = 0
        self.assertEqual(self.account.cash_deposit(deposit_amount), initial_balance)
        self.assertEqual(self.account.balance, initial_balance)

    def test_cash_withdraw_valid(self):
        initial_balance = self.account.balance  # initial_balance is 1000
        withdraw_amount = 300
        returned_balance = self.account.cash_withdraw(withdraw_amount)
        self.assertEqual(returned_balance, initial_balance)  # Should not change
        self.assertEqual(self.account.balance, initial_balance)  # Balance should remain the same

    #def test_cash_withdraw_valid(self):
     #   initial_balance = self.account.balance
      #  withdraw_amount = 300
       # self.assertEqual(self.account.cash_withdraw(withdraw_amount), initial_balance - withdraw_amount)
        #self.assertEqual(self.account.balance, initial_balance - withdraw_amount)

    def test_cash_withdraw_exact_available(self):
        # Withdraw the maximum allowed (balance - 1000)
        self.account.balance = 1500
        withdraw_amount = 500
        self.assertEqual(self.account.cash_withdraw(withdraw_amount), 1000)
        self.assertEqual(self.account.balance, 1000)

    def test_cash_withdraw_insufficient_below_minimum(self):
        self.account.balance = 900
        withdraw_amount = 100
        self.assertEqual(self.account.cash_withdraw(withdraw_amount), 900)
        self.assertEqual(self.account.balance, 900)

    def test_cash_withdraw_insufficient_above_minimum(self):
        self.account.balance = 1200
        withdraw_amount = 300  # Would bring balance below 1000
        self.assertEqual(self.account.cash_withdraw(withdraw_amount), 1200)
        self.assertEqual(self.account.balance, 1200)

    def test_cash_withdraw_negative(self):
        initial_balance = self.account.balance
        withdraw_amount = -100
        self.assertEqual(self.account.cash_withdraw(withdraw_amount), initial_balance)
        self.assertEqual(self.account.balance, initial_balance)

    def test_cash_withdraw_zero(self):
        initial_balance = self.account.balance
        withdraw_amount = 0
        self.assertEqual(self.account.cash_withdraw(withdraw_amount), initial_balance)
        self.assertEqual(self.account.balance, initial_balance)

    def test_monthly_interest(self):
        initial_balance = self.account.balance
        rate = 3.5 / 12
        expected_interest = (initial_balance * rate) / 100
        expected_balance = initial_balance + expected_interest
        result = self.account.monthly_interest(rate)
        self.assertAlmostEqual(result, expected_balance, places=2)
        self.assertAlmostEqual(self.account.balance, expected_balance, places=2)

    def test_loan_repayment_valid_3_years(self):
        capital = 36000
        months = 36
        rate = 8.5
        interest = (capital * months * (rate / 100)) / 12
        expected_payment = (capital + interest) / months
        result = self.account.loan_repayment(capital, months)
        self.assertAlmostEqual(result, expected_payment, places=2)

    def test_loan_repayment_valid_5_years(self):
        capital = 60000
        months = 60
        rate = 12.5
        interest = (capital * months * (rate / 100)) / 12
        expected_payment = (capital + interest) / months
        result = self.account.loan_repayment(capital, months)
        self.assertAlmostEqual(result, expected_payment, places=2)

    def test_loan_repayment_valid_7_years(self):
        capital = 84000
        months = 84
        rate = 17.5
        interest = (capital * months * (rate / 100)) / 12
        expected_payment = (capital + interest) / months
        result = self.account.loan_repayment(capital, months)
        self.assertAlmostEqual(result, expected_payment, places=2)

    def test_loan_repayment_valid_over_7_years(self):
        capital = 120000
        months = 120
        rate = 20
        interest = (capital * months * (rate / 100)) / 12
        expected_payment = (capital + interest) / months
        result = self.account.loan_repayment(capital, months)
        self.assertAlmostEqual(result, expected_payment, places=2)

    def test_loan_repayment_invalid_duration(self):
        capital = 10000
        months = 12
        self.assertIsNone(self.account.loan_repayment(capital, months))
