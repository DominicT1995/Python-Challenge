# Python-Challenge

UTSA Data Analytics Bootcamp Python challenge containing PyBank and PyPoll challenge folders.

------------------------------------------------------------------------------------------------------------------
PYBANK

The PyBank challenge folder contains the Resources folder which contains the budget_data.csv file where the data will be extracted from. 

The main.py file in the PyBank folder utilizes python code to open and read the budget_data.csv file, which the code will then iterate through to perform calculations for financial analysis on the budget data.

Financial analysis will include total months in the analysis, total profits, average change in profits from month to month, greatest increase in profits from month to month, and greatest decrease in profits from month to month.

Upon running the main.py file in the PyBank folder, the financial analysis will be printed to the terminal and written to a budget_analysis.txt file that is located in the Analysis folder within the PyBank folder.

------------------------------------------------------------------------------------------------------------------
PYPOLL

The PyPoll challenge folder contains the Resources folder which contains the election_data.csv file where the data for this challenge will be extracted from.

The main.py file in the PyPoll folder utilizes python code to open and read the election_data.csv file, which the code will read and then convert into a list in order to perform multiple iterations to determine candidates participating in the poll, the number of votes each candidate obtained, the total votes in the poll, the percentage of votes each candidate obtained, and the winner of the poll.

The code is written so that these values can be determined from any variance of poll csv data presented so long as the csv is formatted in a similar manner with the same indexes as the election_data.csv file. 

Upon running the main.py file in the PyPoll folder, the poll results will be printed to the terminal and written to a election_analysis.txt file that is located in the Analysis folder within the PyPoll folder.