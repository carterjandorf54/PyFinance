import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

# Function to read in the CSV File and Create a Pandas DataFrame
# Returns a dictionary of all transactions and DataFrame with the transactions
def readCSV(path):
    with open(path, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Create the List of Dates for DataFrame
        # Create the List of Money Spent for DataFrame
        # Create the List of Categories for Spending
        # Create the List of Account Names
        dateList = []
        moneyspent = []
        category = []
        account = []

        for x in csv_reader:
            dateList.append(x["Date"])
            moneyspent.append(x["Amount"])
            category.append(x["Category"])
            account.append(x["Account Name"])

        # Cast the amount spent to a float
        for i in range(len(moneyspent)):
            moneyspent[i] = float(moneyspent[i])
        
        # Add the List to a Dictionary
        transactions = {"Date" : dateList, "Amount" : moneyspent, "Category" : category, "Account" : account}

        # Create the Pandas DataFrame
        df = pd.DataFrame(transactions)

        # Return the Transactions Dictionary and DataFrame
        return df

# Returns a simple dataframe with all fields from CSV File    
def easyReadCSV(path):
    transactions = pd.read_csv(path)
    return transactions

# Returns a list of categories from the CSV File
def getCategories(df):
    categories = []

    for x in df["Category"]:
        if x in categories:
            pass
        else:
            categories.append(x)
    
    return categories

# Returns the date range from your last to first transaction
def getComplexDateRange(df):
    dateRange = []
    dates = []

    for x in df["Date"]:
        dates.append(x)

    temp_first = dates[-1].split("/")
    first_date = f"{temp_first[2]}-{temp_first[0]}"
    temp_last = dates[0].split("/")
    last_date = f"{temp_last[2]}/{temp_last[0]}"

    dateRange.append(first_date)
    dateRange.append(last_date)

    return dateRange

def getSimpleDateRange(df):
    dateRange = []
    dates = []

    for x in df["Date"]:
        dates.append(x)

    dateRange.append(dates[-1])
    dateRange.append(dates[0])

    return dateRange

    
df = readCSV("assets\Carter_Finances_6_22_23.csv")

x = getSimpleDateRange(df)
y = getCategories(df)

newdf = df[df.Category.isin(["Paycheck"])]
newdf["Total Earned"] = newdf["Amount"].cumsum() 

# Plot Date vs Amount Made
fig, ax = plt.subplots()
ax.plot(newdf["Date"], newdf["Total Earned"])


# Plot Styling
ax.set_title("Date vs Amount Made")
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Total Amount ($)")
ax.tick_params(labelsize=8)

plt.show()

'''
ts = pd.Series(newdf["Amount"], index=newdf["Date"])
ts.plot()
plt.show()
'''



