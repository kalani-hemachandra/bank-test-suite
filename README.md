# ABC Bank Python System
Refer to full instructions in the conversation...

# ABC Bank Application - Testing

## Description

The ABC Bank Application is a Python-based banking system. It provides functionalities for depositing and withdrawing cash, viewing account balance, and calculating loan repayment. This version is designed for testing the core banking logic.

## Features

* **Account Management:**
    * View account balance.
* **Transactions:**
    * Deposit cash into the account.
    * Withdraw cash from the account.
* **Loan Repayment:**
    * Calculate monthly loan repayment amount based on loan amount and duration.

## Technologies Used

* Python

## Prerequisites

* Python 3.x

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd abc_bank_system
    ```

    (Replace `<repository_url>` with the actual URL of your repository)

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application:**

    ```bash
    python bank/app.py
    ```

## Project Structure

```        
abc_bank_system/
├── bank/
│   ├── init.py
│   └── app.py # Main application logic
├── tests/ # (Optional) Test files
│   ├── integration/
│   │   └── test_integration.py
│   ├── performance/
│   │   └── test_performance.py
│   └── system/
│   │   └── test_system.py
│   ├── unit/
│   │   └── test_unit.py
│   └── screenshot_util.py
├── requirements.txt # Dependencies
└── README.md        # Documentation
```

## How to Use

The application is a command-line interface (CLI).  When you run it, you will be able to interact with the banking functions by entering options in the terminal.

## Testing

To test the application, you can use the following methods:

* **Manual Testing:** Run the application and interact with the CLI to test the different functionalities.
* **Automated Testing:** (Recommended)  Write unit tests using a testing framework like `unittest` or `pytest` to verify the behavior of the `BankAccount` class.  Example tests would include:
    * Verifying that the initial balance is correct.
    * Verifying that deposits and withdrawals update the balance correctly.
    * Verifying that the loan repayment calculation is correct for different loan terms.
    * Verifying error handling for invalid inputs (e.g., negative deposit amounts).

## Contributing

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Commit your changes.
4.  Push to the branch.
5.  Submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Author

Kalani Hemachandra
