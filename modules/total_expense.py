import pandas as pd
from datetime import datetime
from user_settings import file_name


def load_data():
    try:
        df = pd.read_excel(f"D:/my projects/price_tracker/{file_name}.xlsx")
        df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
        return df
    except Exception as e:
        print("Error loading expenses file:", e)
        return None


# Today
def get_todays_expense():
    df = load_data()
    if df is None: 
        return
    today = datetime.now().date()  # get today's date
    todays_total = df.loc[df["Date"].dt.date == today, "Amount"].sum()
    print(f"💰 Today's Expense ({today.strftime('%d-%m-%Y')}): ₹{todays_total}")

# Daily Summary
def get_daily_summary():
    df = load_data()
    if df is None: 
        return
    daily_total = df.groupby(df["Date"].dt.date)["Amount"].sum()

    print("📅 Daily Expense Summary:")
    for day, amount in daily_total.items():
        print(f"{day.strftime('%d-%m-%Y')}: ₹{amount}")

# Monthly Summary
def get_monthly_summary():
    df = load_data()
    if df is None: 
        return
    monthly_total = df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum()

    print("📅 Monthly Expense Summary:")
    for period, amount in monthly_total.items():
        month_name = period.strftime("%B %Y")
        print(f"{month_name:<15} ₹{amount}")

# yearly total
def get_yearly_summary():
    df = load_data()
    if df is None: 
        return
    yearly_total = df.groupby(df["Date"].dt.year)["Amount"].sum()

    print("📅 Yearly Expense Summary:")
    for year, amount in yearly_total.items():
        print(f"{year}: ₹{amount}")

# except Exception as e:
#     print("error!")