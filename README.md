# Simple Banking System — Python

This project was developed as a programming exercise solved in Python to practice logic, data structures, and exception handling by simulating a basic banking management system.

---

## About the Project

The system registers clients, processes deposits and withdrawals, generates individual account statements, and displays general statistics about all registered accounts.

The project also uses exception handling to manage invalid inputs and improve execution safety.

---

## Concepts Used

- Lists and dictionaries
- Tuples and sets
- Conditional statements
- `for` loops
- Nested data structures
- Exception handling (`try`, `except`, `raise`, `finally`)
- Financial data manipulation

---

## Features

- Client registration with initial balance
- Deposit and withdrawal processing
- Transaction history for each client
- Identification of accounts with negative balance
- Individual bank statement generation
- Total balance calculation
- Highest and lowest balance identification
- Balance lookup by client ID
- Error handling for invalid inputs

---

## Project Structure

```bash
📁 simple-banking-system
 ├── banking_system.py
 └── README.md
```

---

## How to Run

Run the main file:

```bash
python banking_system.py
```

---

## Example Output

```bash
--- Registered Clients ---
Ana Lima - CPF: 111.111.111-11 - Balance: $1500.00

--- Accounts with Negative Balance ---
- Diego Melo

--- Statement: Ana Lima ---
deposit: $500.00
withdrawal: $300.00
Final balance: $1700.00
```

---

## Author

Pedro Gaudencio
