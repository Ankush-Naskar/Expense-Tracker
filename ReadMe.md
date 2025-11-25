# 📊 EXPENSE-TRACKER
## 🧠 INTRODUCTION
EXPENSE-TRACKER is a lightweight expense management tool built in Python. It helps users record daily spending, organize purchases by category, and automatically generate summaries—including daily, monthly, and yearly reports. Designed for speed and simplicity, it removes the need for spreadsheets or Excel skills, making expense tracking effortless and automated.


## TABLE OF CONTENT
1. [💡 HOW IT WORKS](#-how-it-works)
2. [✨ FEATURES](#-features)
3. [📁 FILE STRUCTURE](#-file-structure)
4. [👤 USER SETTINGS](#-user-settings)
5. [🔐 PRIVACY NOTICE](#-privacy-notice)
6. [⚙️ INSTALLATION](#️-installation)

## 💡 HOW IT WORKS
- The user selects a category, enters a product name and amount.
- The system automatically adds the current date and saves the entry to an Excel file.
- Summary functions analyze the data and display total expenses by day, month, or year.
- All inputs are validated to prevent crashes or incorrect entries.

## ✨ FEATURES
### 🗃️ Add Expense
- Creates `.xlsx` file automatically on first run  
- Appends new expenses to the same file  
- Keeps all records organized in one place


### 📅 Auto-date
Every entry is automatically saved with the current date — users cannot manually select or enter a custom date within EXPENSE-TRACKER. If needed, the date can be edited later directly from the generated `.xlsx` file. To avoid calculation errors in date-based summaries, the format must remain `DD-MM-YYYY`.

### 📊 Summaries
EXPENSE-TRACKER can generate clear spending summaries based on the user’s preference — including daily, monthly, and yearly expense reports. This helps users easily understand their spending patterns and manage their finances better.

## 📁 FILE STRUCTURE
```
📁 EXPENSE-TRACKER/ 
├── 📄 main.py 
|          Entry point for the program 
|
├── 📄 ReadMe.txt 
|           Project documentation 
|
├── 📄 requirements.txt   
|           Dependencies
|
├── 📄 user_settings.py  
|           User-defined categories
|
├── 📁 modules/ 
|  |
│  ├── 📄 add_expense.py 
|  |             Handles input and Excel saving 
|  |
│  ├── 📄 total_expense.py 
|  |             Reporting functions (today, daily, monthly, yearly) 
|  |
└──└── 📄 comments.py 
                Menu display functions 

```


## 👤 USER SETTINGS
- `addCategories` in `user_settings.py` file defines the default expense categories used by EXPENSE-TRACKER. You can customize or expand the list based on your needs:
```python
addCategories = ["clothes", "utilities", "entertainment"]
```  
- You can customize the Excel file name by setting the `file_name` variable:
```python
file_name = "expenses"
```
By default, the file will be named `expenses.xlsx`. You can change this to create and manage multiple files—just assign a different name and use it consistently when adding or accessing data.

All file paths in the program use this format:
```python
"D:\my projects\price_tracker\{file_name}.xlsx"
```
Make sure the file name matches exactly when switching between different expense files.

## 🔐 PRIVACY NOTICE
All expense data is stored locally in a `.xlsx` file. Nothing is uploaded, synced, or shared online. Users are fully responsible for managing, securing, and backing up their own data.

## ⚙️ INSTALLATION
If user want to create a virtual environment
```python
pip install virtualenv          # Install virtualenv
python -m venv env              # Create a virtual environment
.\env\Scripts\activate.ps1      # Activate the environment (Windows PowerShell)
pip install -r requirements.txt # Install required modules

```
 If user don't want to create environment
 ```python
pip install -r requirements.txt # Install required modules
 ```

## 👤 AUTHOR AND CONTACT
ANKUSH NASKAR  
STUDENT  
📬 Email: ankush29607@gmail.com  
🔗 [Linked](https://www.linkedin.com/in/ankush-naskar-4b135438b/)  
🔗 [GitHub](https://github.com/Ankush-Naskar)