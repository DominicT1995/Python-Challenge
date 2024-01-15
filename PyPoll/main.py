# import modules to open, read, and write to the .csv file
import os
import csv

# initialize variables for empty list and dictionary that will store iterated values, and for integer values which will keep tallies
candidates = []
votes = {}
x = 0
total_votes = 0
most_votes = 0

# path to .csv file in Resources folder, open file, and read file from start
poll_csv = os.path.join("Resources", "election_data.csv")

with open(poll_csv) as poll_file:

    poll_reader = csv.reader(poll_file, delimiter=",")

    # define reader as a list so that it can be iterated through multiple times
    poll_list = list(poll_reader)

    # remove the header from the list
    poll_list.pop(0)

    # iterate through poll as a list by row
    for row in poll_list:

        # if the candidate name is not present in list candidates, append the name to the list
        if row[2] not in candidates:

            candidates.append(row[2])

            # then from candidates list, add candidate to dictionary with a value pair of 0 which will be used to count votes per candidate later
            votes[candidates[x]] = 0

            # add one to x to move index for candidates to the next added candidate to add to dictionary
            x = x + 1

    # iterate through candidates list for each candidate
    for candidate in candidates:

        # reset count for votes to zero for each candidate in candidates list
        count = 0

        # for each candidate, iterate through poll list
        for row in poll_list:

            # if iterated candidate is same as candidate in row representing a single vote, add 1 to count
            if candidate == row[2]:

                count = count + 1

        # after poll list is iterated through and count for candidate is complete, set value for candidate key to count to track their votes recieved
        votes[candidate] = count

        # add count for candidate to a grand total of votes cast
        total_votes = total_votes + count

# path to analysis folder for output and write our text list variable into the file
analysis_path = os.path.join("Analysis", "election_analysis.txt")

with open (analysis_path, "w") as analysis_file:

    # initialize empty text list to hold strings used to write to .txt file
    text = []
           
    # print results to terminal using f'strings and append them to our text list as string types
    print('Election Results\n-------------------------')
    text.append('Election Results\n-------------------------')

    print(f'Total Votes: {total_votes}\n-------------------------')
    text.append('\nTotal Votes: ' + str(total_votes) + '\n-------------------------')

    # iterate through each candidate in our votes dictionary
    for candidate in votes:

        # for each candidate in votes dictionary, print to terminal and store in text list candidate name, calculated result for percent votes recieved, and votes recieved
        print(f'{candidate}: {round(votes[candidate]/total_votes * 100, 3)}% ({votes[candidate]})')
        text.append('\n' + str(candidate) + ': ' + str(round(votes[candidate]/total_votes * 100, 3)) + '% (' + str(votes[candidate]) + ')')

        # if value pair denoting vote count from votes dictionary is greater than most_votes, most_votes will equal the new largest vote count and that key value will be denoted as winner
        if votes[candidate] > most_votes:

            most_votes = votes[candidate]

            winner = candidate

    # print resulting winner to terminal and append to text list
    print(f'-------------------------\nWinner: {winner}\n-------------------------')
    text.append('\n-------------------------\nWinner: ' + winner + '\n-------------------------')
    
    # output list of text lines to .txt file in analysis
    analysis_file.writelines(text)