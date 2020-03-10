import os
import csv

csvpath = os.path.join ('C:/', 'Users', 'hongy','Desktop','python-challenge', 'PyPoll', 'election_data.csv')

candidate_list = []
total_votes = 0
candidate_1 = 0
candidate_2 = 0
candidate_3 = 0
candidate_4 = 0
candidate_1_per = 0
candidate_2_per = 0
candidate_3_per = 0
candidate_4_per = 0
winner = { }

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader (csvfile, delimiter = ',')
    header = next(csvreader)
    for row in csvreader:
        total_votes = total_votes + 1

        if str(row[2]) not in candidate_list:
            candidate_list.append(str(row[2]))

        if str(row[2]) == candidate_list[0]:
            candidate_1 = candidate_1 + 1
        elif str(row[2]) == candidate_list[1]:
            candidate_2 = candidate_2 + 1
        elif str(row[2]) == candidate_list[2]:
            candidate_3 = candidate_3 + 1
        else:
            candidate_4 = candidate_4 + 1

        candidate_1_per = round(candidate_1 / total_votes*100, 3)
        candidate_2_per = round(candidate_2 / total_votes*100, 3)
        candidate_3_per = round(candidate_3 / total_votes*100, 3)
        candidate_4_per = round(candidate_4 / total_votes*100, 3)

    winner = {candidate_1_per: candidate_list[0], candidate_2_per: candidate_list[1], candidate_3_per: candidate_list[2], candidate_4_per: candidate_list[3]}

    overall_winner = max(winner.items(), key = lambda x: x[0])

    print("Election Results")
    print("-----------------------------------")
    print(f'Total Votes: ' + str(total_votes))
    print("-----------------------------------")
    print(str(candidate_list[0]) + ": " + str(candidate_1_per) + "% (" + str(candidate_1) + ")")
    print(str(candidate_list[1]) + ": " + str(candidate_2_per) + "% (" + str(candidate_2) + ")")
    print(str(candidate_list[2]) + ": " + str(candidate_3_per) + "% (" + str(candidate_3) + ")")
    print(str(candidate_list[3]) + ": " + str(candidate_4_per) + "% (" + str(candidate_4) + ")")
    print("-----------------------------------")
    print(f'Winner: ' + overall_winner[1])
