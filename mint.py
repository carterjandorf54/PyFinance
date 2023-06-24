import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from MintMethods import MintMethods as mint

path = "assets\Carter_Finances_6_22_23.csv"

x = mint(path)
print(x.date_range)  
#print(x.df)
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



