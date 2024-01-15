# import modules to open, read, and write to the .csv file
import os
import csv

# initialize variables for empty lists that will store iterated values
months = []
profits = []
change = []
stored_value = 0

# path to .csv file in Resources folder, open file, and read file from start
budget_csv = os.path.join("Resources/budget_data.csv")

with open(budget_csv) as budget_file:
    
    budget_reader = csv.reader(budget_file, delimiter=",")

    # move to next line of .csv file to skip header strings
    next(budget_reader)

    # iterate through .csv file by each row being represented as a list
    for row in budget_reader:

        # append month into the months list
        months.append(row[0])

        # append profits into the profits list as integer value
        profits.append(int(row[1]))
        
        # append profit as integer value minus stored_value into change list
        # then set stored_value as current profit to calculate change in profit on next iteration
        change.append(int(row[1]) - stored_value)
        stored_value = int(row[1])

    # determine highest and lowest change by acquiring the index of where max and min change occurred and applying to the months list
    highest_month = months[change.index(max(change))]
    lowest_month = months[change.index(min(change))]
    
    # remove the first item from change list which isn't representative of a month to month change for calculations
    change.pop(0)

    # print results to terminal using f'strings with calculations from lists resulting from iterating through .csv file
    print('Financial Analysis\n----------------------------')
    print(f'Total Months: {len(months)}')
    print(f'Total: ${sum(profits)}')
    print(f'Average Change: ${round(sum(change)/len(change), 2)}')
    print(f'Greatest Increase in Profits: {highest_month} (${max(change)})')
    print(f'Greatest Decrease in Profits: {lowest_month} (${min(change)})')

# define results as a list and convert calculations to string format
text = ['Financial Analysis\n----------------------------', '\nTotal Months: ' + str(len(months)), '\nTotal: $' + str(sum(profits)), '\nAverage Change: $' + str(round(sum(change)/len(change), 2)), '\nGreatest Increase in Profits: ' + highest_month + ' ($' + str(max(change)) + ')', '\nGreatest Decrease in Profits: ' + lowest_month + ' ($' + str(min(change)) + ')']

# path to analysis folder for output and write our text list variable into the file
analysis_path = os.path.join("Analysis", "budget_analysis.txt")

with open (analysis_path, 'w') as analysis_file:

    analysis_file.writelines(text)