import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from MintMethods import MintMethods as mint

path = "assets\Carter_Finances_6_22_23.csv"
user = "Carter Jandorf"

print(f"Hello, Welcome {user}!")
num_filter = int(input("How many Categories would you like to filter from: "))
filter_list = []

x = mint(path)

for i in range(len(x.categories)):
    if ((i+1) % 3) == 0 and i != 0:
        print("%2d %-30s" % (i, x.categories[i]))
    else:
        print("%2d %-30s" % (i, x.categories[i]), end="")
        #print(f"{i}. {x.categories[i]}", end="\t\t")

for i in range(0, num_filter):
    temp = int(input(f"\nEnter choice {i+1}: "))
    filter_list.append(x.categories[temp])

x.dataFilter(x.df, filter_list)
print(x.filtered)
#print(x.filtered["Amount"].sum())
'''
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
'''
ts = pd.Series(newdf["Amount"], index=newdf["Date"])
ts.plot()
plt.show()
'''



