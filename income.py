import json

# Error Checking for FileNotFound Error
try:
    # Open the Json File with the Tax Brackets
    with open("federaltaxes.json", "r") as openfile:
        fed = json.load(openfile)
except FileNotFoundError:
    # Set taxes to 0 if the file cannot be found
    fed = 0

# Define class Income
class Income():

    # Initialize the class with salary
    def __init__(self, salary, tax=0):
        self.salary = salary
        self.tax = tax
        self.netIncome = self.calcNetIncome()

    # Function to calculate the federal tax
    # Input to this file is based on the yearly income declared on init
    # Tax Brackets Pulled from Json File
    # Returns a -1 if improper file call
    def calcFederal(self):

        if fed == 0:
            return -1

        total = 0
        if self.salary >= fed['bracket1'][1] and self.salary <= fed['bracket1'][2]:
            total = self.salary * fed['bracket1'][0]
        elif self.salary >= fed['bracket2'][1] and self.salary <= fed['bracket2'][2]:
            total = (self.salary - fed['bracket1'][2]) * fed['bracket2'][0] + fed['bracket2'][-1]
        elif self.salary >= fed['bracket3'][1] and self.salary <= fed['bracket3'][2]:
            total = (self.salary - fed['bracket2'][2]) * fed['bracket3'][0] + fed['bracket3'][-1]
        elif self.salary >= fed['bracket4'][1] and self.salary <= fed['bracket4'][2]:
            total = (self.salary - fed['bracket3'][2]) * fed['bracket4'][0] + fed['bracket4'][-1]
        elif self.salary >= fed['bracket5'][1] and self.salary <= fed['bracket5'][2]:
            total = (self.salary - fed['bracket4'][2]) * fed['bracket5'][0] + fed['bracket5'][-1]
        elif self.salary >= fed['bracket6'][1] and self.salary <= fed['bracket6'][2]:
            total = (self.salary - fed['bracket5'][2]) * fed['bracket6'][0] + fed['bracket6'][-1]
        else:
            total = (self.salary - fed['bracket6'][1]) * fed['bracket6'][0] + fed['bracket6'][-1]

        return total
    
    def calcSocialSec(self):
        return self.salary * 0.062
    
    def calcMedicare(self):
        return self.salary * 0.0145
    
    def calcNetIncome(self):
        return self.salary - self.calcFederal() - self.calcSocialSec() - self.calcMedicare()


    