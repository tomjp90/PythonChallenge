import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')
vote_analysis = os.path.join("output", "Vote_Analysis_.txt")

votes = []
names = []
unique_candidates = []
percentage_votes = []
total_votes = 0
votes_candidate = []

with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_reader) #skip header row

    for row in csv_reader:
        total_votes = total_votes + 1
        #print(total_votes)

        if row[2] not in unique_candidates:
        #https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
            unique_candidates.append(row[2])
            index = unique_candidates.index(row[2])
            #print(index)
            #print(unique_candidates)
            votes.append(1)

        if row[2] in unique_candidates:
            index = unique_candidates.index(row[2])
            #print(index) 
            votes[index] += 1
            #print(votes)
            #print(unique_index)
            #print(unique_candidates)

    votes_candidate_zip = zip(unique_candidates,votes)
    votes_candidate_list = list(votes_candidate_zip)

    #print(unique_candidates)
    #print(votes)
    #print(votes_candidate_list)
    #print(total_votes)
    percentage_results = []
   
    for i in range(0, len(votes)):  
        percentage_results.append(votes[i]/total_votes)
        
    winner_votes = max(votes)
    #print(winner_votes)
    winner_index = votes.index(winner_votes) 
    #print(winner_index)
    winner_candidate = unique_candidates[winner_index]
    #print(winner_candidate)
    one_name = []
    two_percentage = []
    three_votes = []
    summary_candidates = []

    #make lists to zip and display in output file
    for m in range(0, len(votes)):
        one_name.append(unique_candidates[m])
        two_percentage.append((str(round(percentage_results[m]*100,2)))+ "%") 
        three_votes.append((str(votes[m]-1)))
   
        summary_candidates = zip(one_name, two_percentage, three_votes)

        #print(tuple(summary_candidates))

#print to terminal
print("Election Results")
print("------------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------------------------------")
for j in range(0, len(votes)):
    print(f"{unique_candidates[j]}: {(str(round(percentage_results[j]*100,2)))}% ({str(votes[j]-1)})")
print("------------------------------------------------------")
print(f"Winner: {winner_candidate}")
print("------------------------------------------------------")


#text file
analysis = ("Election Result \n"
"------------------------------------------------------\n"
f"Total Votes: {total_votes}\n"
"------------------------------------------------------\n"
f"{tuple(summary_candidates)}\n"
"------------------------------------------------------\n"
f"Winner: {winner_candidate}\n"
"------------------------------------------------------\n") 

with open(vote_analysis, "w") as txt_file: 
    txt_file.write(analysis)




