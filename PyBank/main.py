
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

    print('Financial Analysis\n----------------------------')
    print(f'Total Months: {len(months)}')
    print(f'Total: ${sum(profits)}')
    print(f'Average Change: ${round(sum(change)/len(change), 2)}')
    print(f'Greatest Increase in Profits: {highest_month} (${max(change)})')
    print(f'Greatest Decrease in Profits: {lowest_month} (${min(change)})')

text = ['Financial Analysis\n----------------------------', '\nTotal Months: ' + str(len(months)), '\nTotal: $' + str(sum(profits)), '\nAverage Change: $' + str(round(sum(change)/len(change), 2)), '\nGreatest Increase in Profits: ' + highest_month + ' ($' + str(max(change)) + ')', '\nGreatest Decrease in Profits: ' + lowest_month + ' ($' + str(min(change)) + ')']

analysis_path = os.path.join("Analysis", "budget_analysis.txt")

with open (analysis_path, 'w') as analysis_file:

    analysis_file.writelines(text)