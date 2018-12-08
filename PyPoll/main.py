import os 
import csv


csv_path = os.path.join('..', 'Resources', 'election_data.csv')

with open(csv_path, 'r', newline='') as csvfile:
    results = csv.reader(csvfile, delimiter=',')

    voter_id = []
    county = []
    candidates = []
    

    #skipping headers
    csv_header = next(csvfile)


    for row in results:
        voter_id.append(int(row[0]))
        candidates.append(str(row[2]))
    
    Khan_vote_count = 0
    Li_vote_count = 0
    Correy_vote_count = 0
    OTooley_vote_count = 0 
    for i, x in enumerate(results):
        if candidates[i] == 'Khan':
            Khan_vote_count += 1



print(Khan_vote_count)

# Total Votes
print('Election Results')
print('--------------------------------------------')
print(f'Total Votes: {len((voter_id))}')
print('--------------------------------------------')


candidate_with_votes = set(candidates)
final_candidate_list = list(candidate_with_votes)
print(final_candidate_list)


print(f'{final_candidate_list[0]}: ')
print(f'{final_candidate_list[1]}: ')
print(f'{final_candidate_list[2]}: ')
print(f'{final_candidate_list[3]}: ')


#print('Election Results')
#print('--------------------------------------------')
#print(f'Total Votes: {len(voter_id)}')
#print(len(county))
#print(f'List of Candidates {candidates}')



#    i = 1
   # for i, x in enumerate(profit_loss)
    #    diff.append(profit_loss[i] - profit_loss[i-1])