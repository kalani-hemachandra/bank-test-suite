class BankAccount:
    def __init__(self):
        # Initialize account balance with the fixed self.balance of 1000
        self.balance = 1000

    def cash_deposit(self, amount):
        # Only accept positive amounts for deposit
        if amount <= 0:
            print("ERROR --> Enter a positive value, try again")
        else:
            self.balance += amount
            print('Net Available Balance: {:.2f}'.format(self.balance))
        return self.balance

    def cash_withdraw(self, amount):
        # Check if the withdrawal amount is positive
        if amount <= 0:
            print("ERROR --> Enter a positive value, try again")
        elif self.balance < 1000:
            print("Insufficient Account Balance! Your balance is below the required 1000 minimum!")
        # Ensure there is enough balance left after withdrawal to maintain the minimum balance of 1000
        elif self.balance - amount >= 1000:
            self.balance -= amount
            print('Net Available Balance: {:.2f}'.format(self.balance))
        else:
            print("Withdrawal request exceeds available funds! Cannot reduce balance below 1000.")
        return self.balance

    def monthly_interest(self, rate):
        # Calculate and apply monthly interest based on rate
        monInt = (self.balance * rate) / 100
        self.balance += monInt
        print('Monthly Interest: {:.2f}'.format(self.balance))
        return self.balance

    def loan_repayment(self, capital, months):
        # Define loan repayment interest rates based on loan duration
        if months < 36:
            print("Oops! Cannot Lend a Loan...")
            return None
        elif months == 36:
            rate = 8.5
        elif months == 60:
            rate = 12.5
        elif months == 84:
            rate = 17.5
        else:
            rate = 20
        interest = (capital * months * (rate / 100)) / 12
        monthly_payment = (capital + interest) / months
        print('Monthly Interest Payment: {:.2f}'.format(monthly_payment))
        return monthly_payment


def welcome_page():
    print("\n Welcome to ABC Bank!!!\n ======================\n")
    print("1 : Cash Deposit")
    print("2 : Cash Withdraw")
    print("3 : Current Balance")
    print("4 : Loan Repayment")
    print("5 : Quit")
    acc_no = input("Enter Account Number: ")
    name = input("Enter Account Holder's Name: ")
    return acc_no, name


if __name__ == "__main__":
    # Instantiate the bank account
    my_acc = BankAccount()
    # Collect account details from the user
    acc, name = welcome_page()

    while True:
        # Display menu options
        option = int(input("\nSelect an option[1-5]: "))
        print("------------------------------------------------")

        if option == 1:
            # Handle deposit option
            amt = float(input("Enter Amount: "))
            my_acc.cash_deposit(amt)
        elif option == 2:
            # Handle withdrawal option
            amt = float(input("Enter Amount: "))
            my_acc.cash_withdraw(amt)
        elif option == 3:
            # Display current balance and monthly interest calculation
            rate = 3.5 / 12  # Example interest rate
            my_acc.monthly_interest(rate)
        elif option == 4:
            # Handle loan repayment calculation
            months = int(input('Enter No of Months: '))
            loan_amt = float(input('Enter Loan Amount: '))
            my_acc.loan_repayment(loan_amt, months)
        elif option == 5:
            # Exit the program
            print("\nThank You For Using Our Service!!\n")
            break
        else:
            # Handle invalid input
            print("\nInvalid Option!!!!")

        # Thank you message
        print("#Thank You For Banking With Us")
