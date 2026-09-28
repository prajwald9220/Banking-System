
from datetime import datetime
import random


# ============================================================
# BANKING MANAGEMENT SYSTEM
# ============================================================


# ============================================================
# CONSTANTS / RULES
# ============================================================

MINIMUM_BALANCE = 1000
MINIMUM_AGE = 18

MAX_ACCOUNTS_PER_CUSTOMER = 1

DAILY_WITHDRAWAL_LIMIT = 50000

MINIMUM_CREDIT_AMOUNT = 100
MINIMUM_DEBIT_AMOUNT = 100
MINIMUM_WITHDRAWAL_AMOUNT = 100

MINIMUM_LOAN_AMOUNT = 10000
MINIMUM_LOAN_TENURE = 6
MAXIMUM_LOAN_TENURE = 360


# Maximum loan amount for each loan type
LOAN_LIMITS = {
    "Home Loan": 5000000,
    "Gold Loan": 1000000,
    "Education Loan": 2000000,
    "Personal Loan": 500000,
    "Vehicle Loan": 1500000,
    "Business Loan": 3000000,
    "Agricultural Loan": 2000000
}


# ============================================================
# DATA STORAGE
# ============================================================

customers = []
accounts = []
transactions = []
loans = []


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def find_customer(customer_id):
    """
    Find customer using customer ID.
    """

    for customer in customers:

        if customer["customer_id"] == customer_id:
            return customer

    return None


def find_account_by_number(account_number):
    """
    Find account using account number.
    """

    for account in accounts:

        if account["account_number"] == account_number:
            return account

    return None


def generate_account_number():
    """
    Generate a unique 10-digit account number.
    """

    while True:

        account_number = str(
            random.randint(1000000000, 9999999999)
        )

        if find_account_by_number(account_number) is None:
            return account_number


def create_transaction(
    account_number,
    transaction_type,
    amount,
    balance_after
):
    """
    Create a transaction record.
    """

    transaction_id = "T" + str(
        len(transactions) + 1
    ).zfill(5)

    transaction = {

        "transaction_id": transaction_id,

        "account_number": account_number,

        "type": transaction_type,

        "amount": amount,

        "balance_after": balance_after,

        "date": datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )
    }

    transactions.append(transaction)


# ============================================================
# 1. CUSTOMER SERVICE
# ============================================================

def add_customer():

    print("\n========== ADD CUSTOMER ==========")

    # ---------------- NAME ----------------

    name = input("Enter customer name: ").strip()

    if name == "":
        print("Customer name cannot be empty.")
        return

    if not name.replace(" ", "").isalpha():

        print(
            "Customer name should contain only alphabets."
        )

        return

    # ---------------- AGE ----------------

    try:

        age = int(
            input("Enter customer age: ")
        )

    except ValueError:

        print("Age must be a number.")
        return

    if age < MINIMUM_AGE:

        print(
            f"Customer must be at least "
            f"{MINIMUM_AGE} years old."
        )

        return

    # ---------------- MOBILE ----------------

    mobile = input(
        "Enter mobile number: "
    ).strip()

    if len(mobile) != 10 or not mobile.isdigit():

        print(
            "Mobile number must contain exactly "
            "10 digits."
        )

        return

    # Check duplicate mobile
    for customer in customers:

        if customer["mobile"] == mobile:

            print(
                "A customer with this mobile "
                "number already exists."
            )

            return

    # ---------------- EMAIL ----------------

    email = input(
        "Enter email: "
    ).strip()

    if email == "":

        print("Email cannot be empty.")
        return

    if "@" not in email or "." not in email:

        print("Please enter a valid email.")
        return

    # Check duplicate email
    for customer in customers:

        if customer["email"] == email:

            print(
                "A customer with this email "
                "already exists."
            )

            return

    # ---------------- ADDRESS ----------------

    address = input(
        "Enter address: "
    ).strip()

    if address == "":

        print("Address cannot be empty.")
        return

    # ---------------- CUSTOMER ID ----------------

    customer_id = "C" + str(
        len(customers) + 1
    ).zfill(4)

    customer = {

        "customer_id": customer_id,

        "name": name,

        "age": age,

        "mobile": mobile,

        "email": email,

        "address": address
    }

    customers.append(customer)

    print("\nCustomer created successfully.")

    print("--------------------------------")

    print(
        "Customer ID :",
        customer_id
    )

    print(
        "Name        :",
        name
    )


# ============================================================

def view_customers():

    print("\n========== ALL CUSTOMERS ==========")

    if not customers:

        print("No customers found.")

        return

    for customer in customers:

        print("\n--------------------------------")

        print(
            "Customer ID :",
            customer["customer_id"]
        )

        print(
            "Name        :",
            customer["name"]
        )

        print(
            "Age         :",
            customer["age"]
        )

        print(
            "Mobile      :",
            customer["mobile"]
        )

        print(
            "Email       :",
            customer["email"]
        )

        print(
            "Address     :",
            customer["address"]
        )


# ============================================================

def search_customer():

    print("\n========== SEARCH CUSTOMER ==========")

    customer_id = input(
        "Enter customer ID: "
    ).strip()

    customer = find_customer(customer_id)

    if customer is None:

        print("Customer not found.")

        return

    print("\nCustomer Found")

    print("--------------------------------")

    print(
        "Customer ID :",
        customer["customer_id"]
    )

    print(
        "Name        :",
        customer["name"]
    )

    print(
        "Age         :",
        customer["age"]
    )

    print(
        "Mobile      :",
        customer["mobile"]
    )

    print(
        "Email       :",
        customer["email"]
    )

    print(
        "Address     :",
        customer["address"]
    )


# ============================================================

def update_customer():

    print("\n========== UPDATE CUSTOMER ==========")

    customer_id = input(
        "Enter customer ID: "
    ).strip()

    customer = find_customer(customer_id)

    if customer is None:

        print("Customer not found.")

        return

    print(
        "\nLeave a field empty if you "
        "do not want to change it."
    )

    # ---------------- NAME ----------------

    name = input(
        "Enter new name: "
    ).strip()

    if name:

        if not name.replace(" ", "").isalpha():

            print(
                "Name should contain only alphabets."
            )

            return

        customer["name"] = name

    # ---------------- MOBILE ----------------

    mobile = input(
        "Enter new mobile number: "
    ).strip()

    if mobile:

        if len(mobile) != 10 or not mobile.isdigit():

            print(
                "Mobile number must contain "
                "exactly 10 digits."
            )

            return

        # Check duplicate mobile
        for other_customer in customers:

            if (
                other_customer["mobile"] == mobile
                and other_customer["customer_id"]
                != customer_id
            ):

                print(
                    "This mobile number already "
                    "belongs to another customer."
                )

                return

        customer["mobile"] = mobile

    # ---------------- EMAIL ----------------

    email = input(
        "Enter new email: "
    ).strip()

    if email:

        if "@" not in email or "." not in email:

            print("Invalid email.")

            return

        for other_customer in customers:

            if (
                other_customer["email"] == email
                and other_customer["customer_id"]
                != customer_id
            ):

                print(
                    "This email already belongs "
                    "to another customer."
                )

                return

        customer["email"] = email

    # ---------------- ADDRESS ----------------

    address = input(
        "Enter new address: "
    ).strip()

    if address:

        customer["address"] = address

    print(
        "\nCustomer updated successfully."
    )


# ============================================================

def delete_customer():

    print("\n========== DELETE CUSTOMER ==========")

    customer_id = input(
        "Enter customer ID: "
    ).strip()

    customer = find_customer(customer_id)

    if customer is None:

        print("Customer not found.")

        return

    # Check account
    for account in accounts:

        if account["customer_id"] == customer_id:

            print(
                "Customer cannot be deleted "
                "because an account exists."
            )

            return

    # Check loan
    for loan in loans:

        if loan["customer_id"] == customer_id:

            print(
                "Customer cannot be deleted "
                "because loan records exist."
            )

            return

    customers.remove(customer)

    print(
        "Customer deleted successfully."
    )


# ============================================================
# CUSTOMER SERVICE MENU
# ============================================================

def customer_service():

    while True:

        print("\n================================")
        print("       CUSTOMER SERVICE")
        print("================================")

        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Back")

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            add_customer()

        elif choice == "2":

            view_customers()

        elif choice == "3":

            search_customer()

        elif choice == "4":

            update_customer()

        elif choice == "5":

            delete_customer()

        elif choice == "6":

            break

        else:

            print(
                "Invalid choice. "
                "Please select 1 to 6."
            )


# ============================================================
# 2. ACCOUNT SECTION
# ============================================================

def create_account():

    print("\n========== CREATE ACCOUNT ==========")

    customer_id = input(
        "Enter customer ID: "
    ).strip()

    customer = find_customer(customer_id)

    # Customer must exist
    if customer is None:

        print("Customer not found.")

        print(
            "Please register the customer first."
        )

        return

    # One account per customer
    account_count = 0

    for account in accounts:

        if account["customer_id"] == customer_id:

            account_count += 1

    if account_count >= MAX_ACCOUNTS_PER_CUSTOMER:

        print(
            "\nAccount creation rejected."
        )

        print(
            "Only one account is allowed "
            "per customer."
        )

        return

    # Initial deposit
    try:

        initial_deposit = float(
            input(
                f"Enter initial deposit "
                f"(minimum ₹{MINIMUM_BALANCE}): "
            )
        )

    except ValueError:

        print("Please enter a valid amount.")

        return

    # Deposit must be positive
    if initial_deposit <= 0:

        print(
            "Initial deposit must be "
            "greater than zero."
        )

        return

    # Minimum balance
    if initial_deposit < MINIMUM_BALANCE:

        print(
            f"Minimum initial deposit "
            f"is ₹{MINIMUM_BALANCE}."
        )

        return

    # Generate account number
    account_number = generate_account_number()

    account = {

        "account_number": account_number,

        "customer_id": customer_id,

        "account_type": "Savings",

        "balance": initial_deposit,

        "minimum_balance": MINIMUM_BALANCE,

        "daily_withdrawal_limit":
            DAILY_WITHDRAWAL_LIMIT,

        "withdrawn_today": 0,

        "status": "Active",

        "created_date":
            datetime.now().strftime("%d-%m-%Y")
    }

    accounts.append(account)

    print("\nAccount created successfully.")

    print("--------------------------------")

    print(
        "Account Number :",
        account_number
    )

    print(
        "Customer ID    :",
        customer_id
    )

    print(
        "Customer Name  :",
        customer["name"]
    )

    print(
        "Account Type   :",
        account["account_type"]
    )

    print(
        "Balance        :",
        f"₹{initial_deposit:.2f}"
    )

    print(
        "Status         :",
        account["status"]
    )


# ============================================================

def find_account():

    account_number = input(
        "Enter account number: "
    ).strip()

    account = find_account_by_number(
        account_number
    )

    return account


# ============================================================

def view_account():

    print("\n========== ACCOUNT DETAILS ==========")

    account = find_account()

    if account is None:

        print("Account not found.")

        return

    print("--------------------------------")

    print(
        "Account Number :",
        account["account_number"]
    )

    print(
        "Customer ID    :",
        account["customer_id"]
    )

    print(
        "Account Type   :",
        account["account_type"]
    )

    print(
        "Balance        :",
        f"₹{account['balance']:.2f}"
    )

    print(
        "Minimum Balance:",
        f"₹{account['minimum_balance']:.2f}"
    )

    print(
        "Daily Limit    :",
        f"₹{account['daily_withdrawal_limit']:.2f}"
    )

    print(
        "Withdrawn Today:",
        f"₹{account['withdrawn_today']:.2f}"
    )

    print(
        "Status         :",
        account["status"]
    )

    print(
        "Created Date   :",
        account["created_date"]
    )


# ============================================================

def check_balance():

    print("\n========== CHECK BALANCE ==========")

    account = find_account()

    if account is None:

        print("Account not found.")

        return

    if account["status"] != "Active":

        print(
            "Account is not active."
        )

        return

    print(
        "Account Number :",
        account["account_number"]
    )

    print(
        "Current Balance:",
        f"₹{account['balance']:.2f}"
    )


# ============================================================

def account_limits():

    print("\n========== ACCOUNT LIMITS ==========")

    print(
        "Maximum accounts per customer :",
        MAX_ACCOUNTS_PER_CUSTOMER
    )

    print(
        "Minimum balance               :",
        f"₹{MINIMUM_BALANCE}"
    )

    print(
        "Daily withdrawal limit        :",
        f"₹{DAILY_WITHDRAWAL_LIMIT}"
    )

    print(
        "Minimum customer age          :",
        MINIMUM_AGE
    )


# ============================================================
# ACCOUNT MENU
# ============================================================

def account_section():

    while True:

        print("\n================================")
        print("          ACCOUNT")
        print("================================")

        print("1. Create Account")
        print("2. View Account")
        print("3. Check Balance")
        print("4. Account Limits")
        print("5. Back")

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            create_account()

        elif choice == "2":

            view_account()

        elif choice == "3":

            check_balance()

        elif choice == "4":

            account_limits()

        elif choice == "5":

            break

        else:

            print(
                "Invalid choice. "
                "Please select 1 to 5."
            )


# ============================================================
# 3. CREDIT / DEBIT
# ============================================================

def credit_money():

    print("\n========== CREDIT MONEY ==========")

    account = find_account()

    if account is None:

        print("Account not found.")

        return

    # Account status
    if account["status"] != "Active":

        print(
            "Credit not allowed."
        )

        print(
            "Account is not active."
        )

        return

    try:

        amount = float(
            input("Enter credit amount: ")
        )

    except ValueError:

        print("Invalid amount.")

        return

    # Amount condition
    if amount < MINIMUM_CREDIT_AMOUNT:

        print(
            f"Minimum credit amount is "
            f"₹{MINIMUM_CREDIT_AMOUNT}."
        )

        return

    account["balance"] += amount

    create_transaction(
        account["account_number"],
        "CREDIT",
        amount,
        account["balance"]
    )

    print(
        "\nMoney credited successfully."
    )

    print(
        "Credit Amount:",
        f"₹{amount:.2f}"
    )

    print(
        "New Balance  :",
        f"₹{account['balance']:.2f}"
    )


# ============================================================

def debit_money():

    print("\n========== DEBIT MONEY ==========")

    account = find_account()

    if account is None:

        print("Account not found.")

        return

    # Account status
    if account["status"] != "Active":

        print(
            "Debit not allowed."
        )

        print(
            "Account is not active."
        )

        return

    try:

        amount = float(
            input("Enter debit amount: ")
        )

    except ValueError:

        print("Invalid amount.")

        return

    # Minimum debit
    if amount < MINIMUM_DEBIT_AMOUNT:

        print(
            f"Minimum debit amount is "
            f"₹{MINIMUM_DEBIT_AMOUNT}."
        )

        return

    # Check balance
    if amount > account["balance"]:

        print(
            "Insufficient balance."
        )

        return

    # Check minimum balance
    remaining_balance = (
        account["balance"] - amount
    )

    if remaining_balance < MINIMUM_BALANCE:

        print(
            "\nDebit rejected."
        )

        print(
            f"Minimum balance of "
            f"₹{MINIMUM_BALANCE} "
            f"must be maintained."
        )

        return

    account["balance"] -= amount

    create_transaction(
        account["account_number"],
        "DEBIT",
        amount,
        account["balance"]
    )

    print(
        "\nMoney debited successfully."
    )

    print(
        "Debit Amount:",
        f"₹{amount:.2f}"
    )

    print(
        "New Balance :",
        f"₹{account['balance']:.2f}"
    )


# ============================================================

def withdraw_money():

    print("\n========== WITHDRAW MONEY ==========")

    account = find_account()

    if account is None:

        print("Account not found.")

        return

    # Account status
    if account["status"] != "Active":

        print(
            "Withdrawal not allowed."
        )

        print(
            "Account is not active."
        )

        return

    try:

        amount = float(
            input("Enter withdrawal amount: ")
        )

    except ValueError:

        print("Invalid amount.")

        return

    # Minimum withdrawal
    if amount < MINIMUM_WITHDRAWAL_AMOUNT:

        print(
            f"Minimum withdrawal amount "
            f"is ₹{MINIMUM_WITHDRAWAL_AMOUNT}."
        )

        return

    # Check balance
    if amount > account["balance"]:

        print(
            "Insufficient balance."
        )

        return

    # Check daily withdrawal limit
    if (
        account["withdrawn_today"] + amount
        > account["daily_withdrawal_limit"]
    ):

        print(
            "\nWithdrawal rejected."
        )

        print(
            "Daily withdrawal limit:",
            f"₹{account['daily_withdrawal_limit']}"
        )

        print(
            "Already withdrawn today:",
            f"₹{account['withdrawn_today']}"
        )

        return

    # Check minimum balance
    remaining_balance = (
        account["balance"] - amount
    )

    if remaining_balance < MINIMUM_BALANCE:

        print(
            "\nWithdrawal rejected."
        )

        print(
            f"Minimum balance of "
            f"₹{MINIMUM_BALANCE} "
            f"must be maintained."
        )

        return

    # Update account
    account["balance"] -= amount

    account["withdrawn_today"] += amount

    create_transaction(
        account["account_number"],
        "WITHDRAW",
        amount,
        account["balance"]
    )

    print(
        "\nWithdrawal successful."
    )

    print(
        "Withdrawn Amount:",
        f"₹{amount:.2f}"
    )

    print(
        "Remaining Balance:",
        f"₹{account['balance']:.2f}"
    )

    print(
        "Today's Withdrawal:",
        f"₹{account['withdrawn_today']:.2f}"
    )


# ============================================================

def transaction_history():

    print(
        "\n========== TRANSACTION HISTORY =========="
    )

    account_number = input(
        "Enter account number: "
    ).strip()

    account = find_account_by_number(
        account_number
    )

    if account is None:

        print("Account not found.")

        return

    found = False

    for transaction in transactions:

        if (
            transaction["account_number"]
            == account_number
        ):

            found = True

            print("--------------------------------")

            print(
                "Transaction ID :",
                transaction["transaction_id"]
            )

            print(
                "Type           :",
                transaction["type"]
            )

            print(
                "Amount         :",
                f"₹{transaction['amount']:.2f}"
            )

            print(
                "Balance After  :",
                f"₹{transaction['balance_after']:.2f}"
            )

            print(
                "Date           :",
                transaction["date"]
            )

    if not found:

        print(
            "No transactions found."
        )


# ============================================================
# CREDIT / DEBIT MENU
# ============================================================

def credit_debit_section():

    while True:

        print("\n================================")
        print("        CREDIT / DEBIT")
        print("================================")

        print("1. Credit Money")
        print("2. Debit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Back")

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            credit_money()

        elif choice == "2":

            debit_money()

        elif choice == "3":

            withdraw_money()

        elif choice == "4":

            check_balance()

        elif choice == "5":

            transaction_history()

        elif choice == "6":

            break

        else:

            print(
                "Invalid choice. "
                "Please select 1 to 6."
            )


# ============================================================
# 4. LOAN SECTION
# ============================================================

# ============================================================
# LOAN ELIGIBILITY CHECK
# ============================================================

def check_loan_eligibility(customer_id):

    customer = find_customer(customer_id)

    # Customer must exist
    if customer is None:

        print("Customer not found.")

        return False

    # Check age
    if customer["age"] < MINIMUM_AGE:

        print("\nLoan Eligibility: NOT ELIGIBLE")

        print(
            f"Customer must be at least "
            f"{MINIMUM_AGE} years old."
        )

        return False

    # Find customer's account
    customer_account = None

    for account in accounts:

        if account["customer_id"] == customer_id:

            customer_account = account
            break

    # Customer must have an account
    if customer_account is None:

        print("\nLoan Eligibility: NOT ELIGIBLE")

        print(
            "Customer must have an account "
            "before applying for a loan."
        )

        return False

    # Account must be active
    if customer_account["status"] != "Active":

        print("\nLoan Eligibility: NOT ELIGIBLE")

        print(
            "Customer account is not Active."
        )

        return False

    # Minimum balance condition
    if customer_account["balance"] < MINIMUM_BALANCE:

        print("\nLoan Eligibility: NOT ELIGIBLE")

        print(
            f"Account must maintain minimum "
            f"balance of ₹{MINIMUM_BALANCE}."
        )

        return False

    # Customer is eligible
    print("\nLoan Eligibility: ELIGIBLE")

    print("--------------------------------")

    print(
        "Customer Name :",
        customer["name"]
    )

    print(
        "Customer Age  :",
        customer["age"]
    )

    print(
        "Account Status:",
        customer_account["status"]
    )

    print(
        "Account Balance:",
        f"₹{customer_account['balance']:.2f}"
    )

    return True



def apply_loan():

    print("\n========== APPLY FOR LOAN ==========")

    customer_id = input(
        "Enter customer ID: "
    ).strip()

    customer = find_customer(customer_id)

    # Customer must exist
    if customer is None:

        print("Customer not found.")

        return

    # ========================================================
    # CHECK LOAN ELIGIBILITY
    # ========================================================

    if not check_loan_eligibility(customer_id):

        print(
            "\nLoan application cannot be processed."
        )

        return

    # ========================================================
    # AVAILABLE LOAN TYPES
    # ========================================================

    print("\nAvailable Loan Types:")

    loan_types = list(
        LOAN_LIMITS.keys()
    )

    for i, loan_type in enumerate(
        loan_types,
        start=1
    ):

        print(
            f"{i}. {loan_type} "
            f"(Maximum ₹"
            f"{LOAN_LIMITS[loan_type]})"
        )

    # ========================================================
    # LOAN TYPE
    # ========================================================

    try:

        choice = int(
            input(
                "Select loan type: "
            )
        )

    except ValueError:

        print(
            "Please enter a valid number."
        )

        return

    if choice < 1 or choice > len(loan_types):

        print(
            "Invalid loan type."
        )

        return

    loan_type = loan_types[
        choice - 1
    ]

    maximum_amount = LOAN_LIMITS[
        loan_type
    ]

    # ========================================================
    # CHECK EXISTING LOAN
    # ========================================================

    for loan in loans:

        if (
            loan["customer_id"] == customer_id
            and loan["loan_type"] == loan_type
            and loan["status"] in
            ["Pending", "Approved"]
        ):

            print(
                "\nLoan application rejected."
            )

            print(
                "Customer already has an "
                "active/pending loan of this type."
            )

            return

    # ========================================================
    # LOAN AMOUNT
    # ========================================================

    try:

        amount = float(
            input("Enter loan amount: ")
        )

    except ValueError:

        print(
            "Loan amount must be a number."
        )

        return

    if amount < MINIMUM_LOAN_AMOUNT:

        print(
            f"Minimum loan amount is "
            f"₹{MINIMUM_LOAN_AMOUNT}."
        )

        return

    if amount > maximum_amount:

        print(
            "\nLoan application rejected."
        )

        print(
            f"Maximum amount for "
            f"{loan_type} is "
            f"₹{maximum_amount}."
        )

        return

    # ========================================================
    # LOAN TENURE
    # ========================================================

    try:

        tenure = int(
            input(
                "Enter tenure in months: "
            )
        )

    except ValueError:

        print(
            "Tenure must be a number."
        )

        return

    if tenure < MINIMUM_LOAN_TENURE:

        print(
            f"Minimum loan tenure is "
            f"{MINIMUM_LOAN_TENURE} months."
        )

        return

    if tenure > MAXIMUM_LOAN_TENURE:

        print(
            f"Maximum loan tenure is "
            f"{MAXIMUM_LOAN_TENURE} months."
        )

        return

    # ========================================================
    # CREATE LOAN
    # ========================================================

    loan_id = "L" + str(
        len(loans) + 1
    ).zfill(4)

    loan = {

        "loan_id": loan_id,

        "customer_id": customer_id,

        "loan_type": loan_type,

        "amount": amount,

        "tenure": tenure,

        "status": "Pending",

        "date":
            datetime.now().strftime(
                "%d-%m-%Y"
            )
    }

    loans.append(loan)

    print(
        "\nLoan application submitted successfully."
    )

    print("--------------------------------")

    print(
        "Loan ID     :",
        loan_id
    )

    print(
        "Customer ID :",
        customer_id
    )

    print(
        "Customer    :",
        customer["name"]
    )

    print(
        "Loan Type   :",
        loan_type
    )

    print(
        "Amount      :",
        f"₹{amount:.2f}"
    )

    print(
        "Tenure      :",
        tenure,
        "months"
    )

    print(
        "Status      :",
        "Successful"
    )


# ============================================================

def view_loans():

    print("\n========== LOAN RECORDS ==========")

    if not loans:

        print(
            "No loan records found."
        )

        return

    for loan in loans:

        print("--------------------------------")

        print(
            "Loan ID     :",
            loan["loan_id"]
        )

        print(
            "Customer ID :",
            loan["customer_id"]
        )

        print(
            "Loan Type   :",
            loan["loan_type"]
        )

        print(
            "Amount      :",
            f"₹{loan['amount']:.2f}"
        )

        print(
            "Tenure      :",
            loan["tenure"],
            "months"
        )

        print(
            "Status      :",
            loan["status"]
        )

        print(
            "Date        :",
            loan["date"]
        )


# ============================================================

def loan_section():

    while True:

        print("\n================================")
        print("          LOAN SECTION")
        print("================================")

        print("1. Apply for Loan")
        print("2. View Loan Records")
        print("3. Back")

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            apply_loan()

        elif choice == "2":

            view_loans()

        elif choice == "3":

            break

        else:

            print(
                "Invalid choice. "
                "Please select 1 to 3."
            )


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n")
        print(
            "=============================================="
        )

        print(
            "       BANKING MANAGEMENT SYSTEM"
        )

        print(
            "=============================================="
        )

        print("1. Customer Service")
        print("2. Account")
        print("3. Credit / Debit")
        print("4. Loan Section")
        print("5. Exit")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        # ---------------- CUSTOMER ----------------

        if choice == "1":

            customer_service()

        # ---------------- ACCOUNT ----------------

        elif choice == "2":

            account_section()

        # ---------------- CREDIT / DEBIT ----------------

        elif choice == "3":

            credit_debit_section()

        # ---------------- LOAN ----------------

        elif choice == "4":

            loan_section()

        # ---------------- EXIT ----------------

        elif choice == "5":

            print(
                "\nThank you for using "
                "Banking Management System."
            )

            break

        # ---------------- INVALID ----------------

        else:

            print(
                "\nInvalid choice."
            )

            print(
                "Please select a number "
                "between 1 and 5."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    main()