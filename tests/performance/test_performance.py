import unittest
import timeit
from bank.app import BankAccount

class TestPerformanceBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount()

    def test_cash_deposit_performance(self):
        deposit_amount = 100
        number_of_runs = 10000

        def deposit():
            self.account.cash_deposit(deposit_amount)

        execution_time = timeit.timeit(deposit, number=number_of_runs)
        average_time = execution_time / number_of_runs
        print(f"\nPerformance Test: {number_of_runs} cash deposits took {execution_time:.4f} seconds (average: {average_time:.8f} seconds per deposit).")

        # You could add assertions here to check if the average time is within an acceptable threshold
        self.assertLess(average_time, 0.0001, "Cash deposit performance is too slow (adjust threshold as needed).")

        # Reset balance after the test
        self.account.balance = 1000

    def test_cash_withdraw_performance(self):
        withdraw_amount = 50
        number_of_runs = 10000
        self.account.balance = 2000  # Ensure sufficient balance for multiple withdrawals

        def withdraw():
            self.account.cash_withdraw(withdraw_amount)

        execution_time = timeit.timeit(withdraw, number=number_of_runs)
        average_time = execution_time / number_of_runs
        print(f"\nPerformance Test: {number_of_runs} cash withdrawals took {execution_time:.4f} seconds (average: {average_time:.8f} seconds per withdrawal).")
        self.assertLess(average_time, 0.0001, "Cash withdrawal performance is too slow (adjust threshold as needed).")

        # Reset balance after the test
        self.account.balance = 1000

    def test_monthly_interest_performance(self):
        rate = 3.5 / 12
        number_of_runs = 10000

        def calculate_interest():
            self.account.monthly_interest(rate)

        execution_time = timeit.timeit(calculate_interest, number=number_of_runs)
        average_time = execution_time / number_of_runs
        print(f"\nPerformance Test: {number_of_runs} monthly interest calculations took {execution_time:.4f} seconds (average: {average_time:.8f} seconds per calculation).")
        self.assertLess(average_time, 0.0002,"Monthly interest calculation performance (with print) is too slow (adjusted threshold).")
        # Reset balance after the test
        self.account.balance = 1000

    def test_loan_repayment_performance_3_years(self):
        capital = 10000
        months = 36
        number_of_runs = 1000

        def repay_loan():
            self.account.loan_repayment(capital, months)

        execution_time = timeit.timeit(repay_loan, number=number_of_runs)
        average_time = execution_time / number_of_runs
        print(f"\nPerformance Test: {number_of_runs} loan repayment calculations (3 years) took {execution_time:.4f} seconds (average: {average_time:.8f} seconds per calculation).")
        self.assertLess(average_time, 0.0001, "Loan repayment calculation performance is too slow (adjust threshold as needed).")

        # No balance to reset here as it's a calculation

# You would need to integrate this into your test execution flow (e.g., run it with other unit tests)