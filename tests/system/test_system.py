import unittest
from unittest.mock import patch
import io
import sys
import os
from bank.app import welcome_page, BankAccount

SCREENSHOTS_DIR = 'screenshots'
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def take_screenshot(test_name):
    filename = os.path.join(SCREENSHOTS_DIR, f"{test_name}.png")
    print(f"Simulating taking screenshot: {filename}")
    with open(filename, 'w') as f:
        f.write(f"Screenshot of {test_name}")

class TestSystemInteraction(unittest.TestCase):
    @patch('builtins.input', side_effect=['1234', 'Kalani', '1', '500', '5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('bank.app.welcome_page', return_value=('1234', 'Kalani'))
    @patch('bank.app.BankAccount', return_value=BankAccount())
    def test_deposit_flow(self, mock_bank_account, mock_welcome_page, stdout_mock, mock_input):
        take_screenshot("test_deposit_flow_start")
        # Simulate the main loop
        my_acc = BankAccount()
        acc, name = welcome_page()
        option = int(input("\nSelect an option[1-5]: "))
        print("------------------------------------------------")
        if option == 1:
            amt = float(input("Enter Amount: "))
            my_acc.cash_deposit(amt)
        print("#Thank You For Banking With Us")
        option = int(input("\nSelect an option[1-5]: "))
        print("------------------------------------------------")
        if option == 5:
            print("\nThank You For Using Our Service!!\n")

        self.assertIn("Welcome to ABC Bank!!!", stdout_mock.getvalue())
        self.assertIn("Net Available Balance: 1500.00", stdout_mock.getvalue())
        self.assertIn("Thank You For Using Our Service!!", stdout_mock.getvalue())
        take_screenshot("test_deposit_flow_end")

    @patch('builtins.input', side_effect=['5678', 'Jane Doe', '2', '200', '5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('bank.app.welcome_page', return_value=('5678', 'Jane Doe'))
    @patch('bank.app.BankAccount', return_value=BankAccount())
    def test_withdraw_flow(self, mock_bank_account, mock_welcome_page, stdout_mock, mock_input):
        take_screenshot("test_withdraw_flow_start")
        my_acc = BankAccount()
        acc, name = welcome_page()
        option = int(input("\nSelect an option[1-5]: "))
        print("------------------------------------------------")
        if option == 2:
            amt = float(input("Enter Amount: "))
            my_acc.cash_withdraw(amt)
        print("#Thank You For Banking With Us")
        option = int(input("\nSelect an option[1-5]: "))
        print("------------------------------------------------")
        if option == 5:
            print("\nThank You For Using Our Service!!\n")

        self.assertIn("Welcome to ABC Bank!!!", stdout_mock.getvalue())
        self.assertIn("Withdrawal request exceeds available funds! Cannot reduce balance below 1000.",
                      stdout_mock.getvalue())
        self.assertIn("Thank You For Using Our Service!!", stdout_mock.getvalue())
        take_screenshot("test_withdraw_flow_end")

    @patch('builtins.input', side_effect=['9012', 'Peter Pan', '3', '5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('bank.app.welcome_page', return_value=('9012', 'Peter Pan'))
    @patch('bank.app.BankAccount', return_value=BankAccount())
    def test_check_balance_flow(self, mock_bank_account, mock_welcome_page, stdout_mock, mock_input):
        take_screenshot("test_check_balance_flow_start")
        my_acc = BankAccount()
        acc, name = welcome_page()
        option = int(input("\nSelect an option[1-5]: "))
        print("------------------------------------------------")
        if option == 3:
            rate = 3.5 / 12
            my_acc.monthly_interest(rate)
        print("#Thank You For Banking With Us")
        option = int(input("\nSelect an option[1-5]: "))
        print("------------------------------------------------")
        if option == 5:
            print("\nThank You For Using Our Service!!\n")

        self.assertIn("Welcome to ABC Bank!!!", stdout_mock.getvalue())
        expected_balance = 1000 + (1000 * 3.5 / 100 / 12)
        self.assertIn(f'Monthly Interest: {expected_balance:.2f}', stdout_mock.getvalue())
        self.assertIn("Thank You For Using Our Service!!", stdout_mock.getvalue())
        take_screenshot("test_check_balance_flow_end")

    @patch('builtins.input', side_effect=['3456', 'Wendy', '4', '36', '10000', '5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('bank.app.welcome_page', return_value=('3456', 'Wendy'))
    @patch('bank.app.BankAccount', return_value=BankAccount())
    def test_loan_repayment_flow(self, mock_bank_account, mock_welcome_page, stdout_mock, mock_input):
        take_screenshot("test_loan_repayment_flow_start")
        my_acc = BankAccount()
        acc, name = welcome_page()
        option = int(input("\nSelect an option[1-5]: "))
        print("------------------------------------------------")
        if option == 4:
            months = int(input('Enter No of Months: '))
            loan_amt = float(input('Enter Loan Amount: '))
            my_acc.loan_repayment(loan_amt, months)
        print("#Thank You For Banking With Us")
        option = int(input("\nSelect an option[1-5]: "))
        print("------------------------------------------------")
        if option == 5:
            print("\nThank You For Using Our Service!!\n")

        self.assertIn("Welcome to ABC Bank!!!", stdout_mock.getvalue())
        expected_payment = (10000 + (10000 * 36 * 8.5 / 100) / 12) / 36
        self.assertIn(f'Monthly Interest Payment: {expected_payment:.2f}', stdout_mock.getvalue())
        self.assertIn("Thank You For Using Our Service!!", stdout_mock.getvalue())
        take_screenshot("test_loan_repayment_flow_end")

    @patch('builtins.input', side_effect=['1111', 'Alice', '5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('bank.app.welcome_page', return_value=('1111', 'Alice'))
    @patch('bank.app.BankAccount', return_value=BankAccount())
    def test_quit_flow(self, mock_bank_account, mock_welcome_page, stdout_mock, mock_input):
        take_screenshot("test_quit_flow_start")
        my_acc = BankAccount()
        acc, name = welcome_page()
        option = int(input("\nSelect an option[1-5]: "))
        print("------------------------------------------------")
        if option == 5:
            print("\nThank You For Using Our Service!!\n")

        self.assertIn("Welcome to ABC Bank!!!", stdout_mock.getvalue())
        self.assertIn("Thank You For Using Our Service!!", stdout_mock.getvalue())
        take_screenshot("test_quit_flow_end")