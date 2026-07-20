# SpendSense

**SpendSense** is a Python-based application designed to help users efficiently manage their personal finances. It allows users to record income and expenses, generate monthly financial reports, and export transaction history to CSV while storing data persistently using JSON.

---

## ✨ Features

*  Add Income
*  Add Expenses
*  View Transaction History
*  Generate Monthly Financial Reports
*  Export Transactions to CSV
*  Persistent Data Storage using JSON

---

## 📂 Project Structure

```text
SpendSense/
│
├── main.py          # Main application and menu
├── finance.py       # Income and expense management
├── storage.py       # JSON load/save operations
├── reports.py       # Transaction reports
├── export.py        # CSV export functionality
├── data.json        # Stores transaction data
└── report.csv       # Generated CSV report
```

---

## 🛠️ Technologies Used

* Python 3
* JSON
* CSV
* Datetime Module

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/FalakJan01/SpendSense.git
```

### 2. Navigate to the Project Directory

```bash
cd SpendSense
```

### 3. Run the Application

```bash
python main.py
```

---

## 📋 Menu

```text
====== SpendSense ======

1. Add Income
2. Add Expense
3. View Transactions
4. Monthly Report
5. Export CSV
6. Exit
```

---

## 📊 Sample Monthly Report

```text
Monthly Report
----------------------
Total Income : ₹50,000
Total Expense: ₹12,500
Savings      : ₹37,500
```

---

## 💾 Data Storage

All transactions are stored in a local **JSON** file (`data.json`), ensuring your financial records remain available even after the application is closed.

---

## 📁 CSV Export

SpendSense allows you to export all recorded transactions into a **CSV** file (`report.csv`), making it easy to open and analyze your financial data in Microsoft Excel, Google Sheets, or any spreadsheet software.

---

## 📚 Key Python Concepts Used

* Functions
* Lists & Dictionaries
* Modular Programming
* File Handling
* JSON Serialization
* CSV Operations
* Loops & Conditional Statements
* Date & Time Handling
* Exception Handling

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository, improve the project, and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

Developed by FJ using Python.
