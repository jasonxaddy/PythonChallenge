import os 
import csv

csv_path = os.path.join('..', 'Resources', 'election_data.csv')

with open(csv_path, 'r', newline='') as csvfile:
    results = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)

    voter_id = []
    county = []
    candidates = []
    
    max_profit = 0
    max_loss = 0
    max_month = []

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




# import os
# import csv
# import pandas as pd

# link = 'https://nu.bootcampcontent.com/NU-Coding-Bootcamp/NUCHI201811DATA2/raw/master/Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv'
# results = pd.read_csv(link)
# print(results)

# # Hello

# csv_path = os.path.join('..', 'Resources', 'election_data.csv')

# with open(csv_path, 'r', newline='') as csvfile:
#     results = csv.reader(csvfile, delimiter=',')
    
#     for _ in results:
#         print('yo, sup?')
# #     votes_cast = 0
#     # candidates = {}

#     # skipping headers
#     #  csv_header = next(results)

#     votes_cast = 0
#     for row in results:
#         votes_cast += 1
#         if row[2] in candidates:
#             candidates[row[2]] = candidates[row[2]] + 1
#         else: 
#             candidates[row[2]] = 1

# print(candidates)

#         # if candidates[row] == 'Khan':
#         #     Khan_vote_count += 1


# # print(votes_cast)
    
# #     Khan_vote_count = 0
# #     Li_vote_count = 0
# #     Correy_vote_count = 0
# #     OTooley_vote_count = 0 
# #     for i, x in enumerate(results):
# #         if candidates[i] == 'Khan':
# #             Khan_vote_count += 1
        
# # print(Khan_vote_count)

# # Total Votes
# print('Election Results')
# print('--------------------------------------------')
# print(f'Total Votes: {len((voter_id))}')
# print('--------------------------------------------')


# candidate_with_votes = set(candidates)
# final_candidate_list = list(candidate_with_votes)
# print(final_candidate_list)


# print(f'{final_candidate_list[0]}: ')
# print(f'{final_candidate_list[1]}: ')
# print(f'{final_candidate_list[2]}: ')
# print(f'{final_candidate_list[3]}: ')


# #print('Election Results')
# #print('--------------------------------------------')
# #print(f'Total Votes: {len(voter_id)}')
# #print(len(county))
# #print(f'List of Candidates {candidates}')



# #    i = 1
#    # for i, x in enumerate(profit_loss)
#     #    diff.append(profit_loss[i] - profit_loss[i-1])
