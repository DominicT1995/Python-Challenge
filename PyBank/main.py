# create a Python script that analyzes the records to calculate each of the following values:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# Total Months: 86 Total: $22564198 Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002) Greatest Decrease in Profits: Feb-14 ($-1825558)

import os
import csv

months = []
profits = []
change = []
stored_value = 0

budget_csv = os.path.join("Resources/budget_data.csv")

with open(budget_csv) as budget_file:
    
    budget_reader = csv.reader(budget_file, delimiter=",")

    next(budget_reader)

    for row in budget_reader:

        months.append(row[0])

        profits.append(int(row[1]))
        
        change.append(int(row[1]) - stored_value)
        stored_value = int(row[1])


    highest_month = months[change.index(max(change))]
    lowest_month = months[change.index(min(change))]

    change.pop(0)

    print(f'Total Months: {len(months)}')
    print(f'Total: ${sum(profits)}')
    print(f'Average Change: ${round(sum(change)/len(change), 2)}')
    print(f'Greatest Increase in Profits: {highest_month} (${max(change)})')
    print(f'Greatest Decrease in Profits: {lowest_month} (${min(change)})')
