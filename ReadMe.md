# 📊 EXPENSE-TRACKER
![POSTER](media/img4.png)
## 🧠 INTRODUCTION
EXPENSE-TRACKER is a lightweight expense management tool built in Python. It helps users record daily spending, organize purchases by category, and automatically generate summaries—including daily, monthly, and yearly reports. Designed for speed and simplicity, it removes the need for spreadsheets or Excel skills, making expense tracking effortless and automated.


## TABLE OF CONTENT
1. [💡 HOW IT WORKS](#-how-it-works)
2. [✨ FEATURES](#-features)
3. [📁 FILE STRUCTURE](#-file-structure)
4. [👤 USER SETTINGS](#-user-settings)
5. [🔐 PRIVACY NOTICE](#-privacy-notice)
6. [⚙️ INSTALLATION](#️-installation)
7. [🚀 FUTURE PLANS](#future-plans)
8. [👤 AUTHOR AND CONTACT](#-author-and-contact)

## 💡 HOW IT WORKS
- The user selects a category, enters a product name and amount.
- The system automatically adds the current date and saves the entry to an Excel file.
- Summary functions analyze the data and display total expenses by day, week, month, or year.
- All inputs are validated to prevent crashes or incorrect entries.

## ✨ FEATURES

### 🗃️ Smart Data Entry
* **Auto-Creation:** Automatically creates the `expenses.xlsx` file on the first run.
* **Batch Entry Mode:** Add multiple expenses in a row without returning to the main menu.
* **Robust Validation:** Prevents crashes by checking user input (e.g., ensures amounts are numbers).

### 📅 Intelligent Summaries
View your financial health with powerful grouping algorithms:
* **🌅 Today:** Quick snapshot of daily spending.
* **📅 Daily:** Day by day expenses for last 365 days 
* **🗓️ Weekly:** breakdown of expenses for the last 8 weeks.
* **🈷️ Monthly:** Month-by-month trends for the 12 months.
* **📅 Yearly:** High-level annual overview.

### ⚙️ Auto-Configuration
* **Self-Healing Settings:** Automatically generates a `user_settings.py` file if one is missing.
* **Customizable:** Easily change category names or the target filename.
### 📈 PIE CHART
Generate a `pie-chart` to for better analysis.(UPCOMING) 
### 📅 Auto-date
Every entry is automatically saved with the current date. Users cannot manually select or enter a custom date within EXPENSE-TRACKER. If needed, the date can be edited later directly from the generated `.xlsx` file. To avoid calculation errors in date-based summaries, the format must remain `DD-MM-YYYY`.



## 📁 FILE STRUCTURE

![file structure](media/img3.png)


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
"{file_name}.xlsx"
```
Make sure the file name matches exactly when switching between different expense files.

## 🔐 PRIVACY NOTICE
All expense data is stored locally in a `.xlsx` file. Nothing is uploaded, synced, or shared online. Users are fully responsible for managing, securing, and backing up their own data.

## ⚙️ INSTALLATION
### 🔧 TOOLS
1. [git](https://git-scm.com/install/windows)  
2. [vs code](https://code.visualstudio.com/Download)  
3. [python](https://www.python.org/downloads/)  

### 🎥 INSTALLATION VIDEO
(COMING SOON)

### 💻 CODES


1. If user want to create a virtual environment:

```bash
pip install virtualenv          # Install virtualenv
python -m venv env              # Create a virtual environment
.\env\Scripts\activate.ps1      # Activate the environment (Windows PowerShell)
pip install -r requirements.txt # Install required modules
```
2. If user don't want to create environment  
 ```bash
pip install -r requirements.txt # Install required modules
 ```

## 🚀 FUTURE PLANS
1. Add category wise analysis
2. Add pie-chart for better understanding
## 👤 AUTHOR AND CONTACT
ANKUSH NASKAR  
STUDENT  
📬 Email: ankush29607@gmail.com  
🔗 [Linkedin](https://www.linkedin.com/in/ankush-naskar-4b135438b/)  
🔗 [GitHub](https://github.com/Ankush-Naskar)