import os
import csv

election_data_csv = os.path.join("..","Resources","election_data.csv")

with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    total_number_votes = 0
    candidates = {}
    candidates_percent = {}
    candidate_vote_max = 0
    candidate_winner = ""

    for row in csvreader:
        total_number_votes = total_number_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidates:
             candidates[candidate_name] = 1
        else:
            candidates[candidate_name] = candidates[candidate_name] + 1

    for candidate_name in candidates:
        candidates_percent[candidate_name] = (candidates[candidate_name]/total_number_votes) * 100
    
    for candidate_name in candidates:
        if candidates[candidate_name] > candidate_vote_max:
            candidate_vote_max = candidates[candidate_name]
            candidate_winner = candidate_name
    
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_number_votes}")
print("-----------------------------")
for candidate_name in candidates_percent:
    print(f'{candidate_name} : {format(candidates_percent[candidate_name],".3f")}% ({candidates[candidate_name]})')
print("-----------------------------")
print(f"Winner: {candidate_winner}")
print("-----------------------------")
        
election_result = os.path.join("..","Analysis","results.txt")

with open(election_result, 'w') as txtfile:
    txtfile.write("Election Results"+ "\n")
    txtfile.write("-----------------------------"+ "\n")
    txtfile.write(f"Total Votes: {total_number_votes}" + "\n")
    txtfile.write("-----------------------------"+ "\n")
    for candidate_name in candidates_percent:
        txtfile.write(f'{candidate_name} : {format(candidates_percent[candidate_name],".3f")}% ({candidates[candidate_name]})'+ '\n')
    txtfile.write("-----------------------------"+ "\n")
    txtfile.write(f"Winner: {candidate_winner}"+ "\n")
    txtfile.write("-----------------------------")


