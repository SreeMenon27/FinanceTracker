# 💰 Finance Tracker – A CLI App for Managing Personal Finances

Welcome to **Finance Tracker**, a simple command-line tool to help you **track your income and expenses**, calculate your **running balance**, and maintain a clean record of transactions — all using **Python**.

This project was developed as part of my learning journey through the **Ultimate Data Science and GENAI Bootcamp** by [Krish Naik Academy](https://www.krishnaik.in/), to solidify my understanding of Python fundamentals, file operations, modular design, and real-world utility.

---

## 🚀 Features

- ✅ Add income and expense transactions  
- ✅ View all transactions in a well-formatted terminal report  
- ✅ Calculate and display the current balance  
- ✅ Save and load transactions from a JSON file  
- ✅ Categorize transactions (e.g., Salary, Food, Transport, etc.)  
- ✅ Automatic timestamping for each transaction  

---

## 🧠 Key Learnings Applied

| Concept | How It Was Used |
|--------|------------------|
| **JSON File Operations** | To save and load transaction records persistently |
| **Private Methods** | Encapsulated internal logic (`_load_transactions`, `_save_transactions`, etc.) |
| **@property Decorator** | Used for dynamic balance calculation |
| **String Formatting** | Clean alignment in terminal reports |
| **Modular Python Design** | Organized code into clear modules (e.g., config, tracker) |
| **Data Structures** | Used lists & dictionaries for transaction storage |
| **Timestamping** | Used `time.strftime()` to log when each transaction was added |
| **Input Validation** | Handled user inputs with error checking and feedback |

---

## 🖥️ Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/SreeMenon27/FinanceTracker.git

# Navigate into the project folder
cd FinanceTracker

# Run the tracker script
python main.py

📁 Project Structure
FinanceTracker/
├── Data/
│   └── records.json         # Stores all transactions
├── Tracker/
│   ├── __init__.py
│   ├── config.py            # Stores income & expense categories
│   └── tracker.py           # Core logic for adding/viewing transactions
├── run_tracker.py           # Entry point
└── README.md                # Project documentation

📸 Preview (Sample Output)
markdown
Copy
Edit
No.  Type       Category           Amount     Timestamp
------------------------------------------------------------
1    income     Salary             5000.00    2025-05-10 14:23:11
2    expense    Groceries          120.00     2025-05-10 15:05:03
3    expense    Utilities          90.00      2025-05-11 09:21:45
------------------------------------------------------------
     Balance                      4790.00
💡 Future Improvements
Add support for monthly summaries

Export reports to CSV or PDF

Add budgeting goals or alerts

Build a GUI version using Tkinter or PyQt

🧑‍💻 Author
Sreekala Menon
📫 Connect with me on LinkedIn
💬 Always learning, always building!

🏷️ Tags
#Python #DataScience #BeginnerProject #CLIApp #FileHandling #JSON #ProjectShowcase