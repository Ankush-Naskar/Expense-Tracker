import pandas as pd
from datetime import datetime, timedelta
from user_settings import file_name


def load_data():
    try:
        df = pd.read_excel(f"{file_name}.xlsx")
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
    print(f"\n💰 Today's Expense ({today.strftime('%d-%m-%Y')}): ₹{todays_total}")

# Daily Summary
def get_daily_summary():
    df = load_data()
    if df is None: return

    cutoff_date = pd.Timestamp.now() - pd.Timedelta(days=365)
    recent_data = df[df["Date"] >= cutoff_date]

    daily_total = recent_data.groupby(recent_data["Date"].dt.date)["Amount"].sum()

    print(f"\n📅 Daily Expense Summary:")

    for day, amount in daily_total.items():
        print(f"{day.strftime('%d-%m-%Y')}: ₹{amount}")
        
# weekly summary 
def get_last_8_weeks_summary():
    df = load_data()
    if df is None: return

    cutoff = pd.Timestamp.now() - pd.DateOffset(weeks=8)
    recent = df[df["Date"] >= cutoff]
    weekly_groups = recent.groupby(recent["Date"].dt.to_period("W"))["Amount"].sum()

    print(f"\n📅 Weekly Summary: ")
    
    for week, amount in weekly_groups.items():
        start = week.start_time.strftime('%d-%m')
        end = week.end_time.strftime('%d-%m')
        
        print(f"({start} to {end}) - ₹{amount}")
        

# Monthly Summary
def get_monthly_summary():
    df = load_data()
    if df is None: return

    cutoff_date = pd.Timestamp.now() - pd.DateOffset(months=12)
    recent_data = df[df["Date"] >= cutoff_date]

    monthly_total = recent_data.groupby(recent_data["Date"].dt.to_period("M"))["Amount"].sum()

    print("\n📅 Monthly Expense Summary (Last 12 Months):")
    
    for period, amount in monthly_total.items():
        month_name = period.strftime("%B %Y")
        print(f"{month_name:<15} ₹{amount}")
        

# yearly total
def get_yearly_summary():
    df = load_data()
    if df is None: 
        return
    yearly_total = df.groupby(df["Date"].dt.year)["Amount"].sum()

    print("\n📅 Yearly Expense Summary:")
    for year, amount in yearly_total.items():
        print(f"{year}: ₹{amount}")

