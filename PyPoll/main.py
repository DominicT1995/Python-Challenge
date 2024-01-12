# calculates each of the following values:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

# Total Votes: 369711 / Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892) / Raymon Anthony Doane: 3.139% (11606)
# Winner: Diana DeGette

import os
import csv

candidates = []
votes = {}
x = 0
total_votes = 0
most_votes = 0

poll_csv = os.path.join("Resources", "election_data.csv")

with open(poll_csv) as poll_file:

    poll_reader = csv.reader(poll_file, delimiter=",")

    poll_list = list(poll_reader)

    poll_list.pop(0)

    for row in poll_list:

        if row[2] not in candidates:

            candidates.append(row[2])

            votes[candidates[x]] = 0

            x = x + 1

    for candidate in candidates:

        count = 0

        for row in poll_list:

            if candidate == row[2]:

                count = count + 1

        votes[candidate] = count

        total_votes = total_votes + count

    print('Election Results\n-------------------------')

    print(f'Total Votes: {total_votes}\n-------------------------')

    for candidate in votes:

        print(f'{candidate}: {round(votes[candidate]/total_votes * 100, 3)}% ({votes[candidate]})')

        if votes[candidate] > most_votes:

            most_votes = votes[candidate]

            winner = candidate

    print(f'-------------------------\nWinner: {winner}\n-------------------------')
    


