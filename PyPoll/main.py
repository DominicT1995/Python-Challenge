
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

analysis_path = os.path.join("Analysis", "election_analysis.txt")

with open (analysis_path, "w") as analysis_file:

    text = []
           
    print('Election Results\n-------------------------')
    text.append('Election Results\n-------------------------')

    print(f'Total Votes: {total_votes}\n-------------------------')
    text.append('\nTotal Votes: ' + str(total_votes) + '\n-------------------------')

    for candidate in votes:

        print(f'{candidate}: {round(votes[candidate]/total_votes * 100, 3)}% ({votes[candidate]})')
        text.append('\n' + str(candidate) + ': ' + str(round(votes[candidate]/total_votes * 100, 3)) + '% (' + str(votes[candidate]) + ')')

        if votes[candidate] > most_votes:

            most_votes = votes[candidate]

            winner = candidate

    print(f'-------------------------\nWinner: {winner}\n-------------------------')
    text.append('\n-------------------------\nWinner: ' + winner + '\n-------------------------')
    
    analysis_file.writelines(text)