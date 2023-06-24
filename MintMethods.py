import csv
import pandas as pd

class MintMethods():

    # Initialize Mint Methods with an Empty DataFrame
    def __init__(self, path):
        self.df = self.readCSV(path)
        self.categories = self.getCategories(self.df)
        self.date_range = self.getSimpleDateRange(self.df)
        self.filtered = pd.DataFrame()

    # Function to read in the CSV File and Create a Pandas DataFrame
    def readCSV(self, path):
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
    def easyReadCSV(self, path):
        transactions = pd.read_csv(path)
        return transactions
    
    # Returns a list of categories from the CSV File
    def getCategories(self, df):
        categories = []

        for x in df["Category"]:
            if x in categories:
                pass
            else:
                categories.append(x)
        
        return categories
    
    def getSimpleDateRange(self, df):
        dateRange = []
        dates = []

        for x in df["Date"]:
            dates.append(x)

        dateRange.append(dates[-1])
        dateRange.append(dates[0])

        return dateRange
    
    # Create a filtered Data Frame Based off category
    def dataFilter(self, df, category):
        filtered = df.loc[(df.Category.isin(category))]
        self.filtered = filtered



        