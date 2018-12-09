import os 
import csv

csv_path = os.path.join('..', 'Resources', 'election_data.csv')

with open(csv_path, 'r', newline='') as csvfile:
    results = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)

    voter_id = []
    county = []
    candidates = []
    Khan_vote_count = 0
    Li_vote_count = 0
    Correy_vote_count = 0
    OTooley_vote_count = 0 
    for row in results:
        voter_id.append(int(row[0]))
        candidates.append(str(row[2]))
    if voter_id == 'Khan':
        Khan_vote_count = Khan_vote_count + 1
    elif voter_id == 'Li':
        Li_vote_count = Li_vote_count + 1
    elif voter_id == 'Correy':
        Correy_vote_count = Correy_vote_count + 1
    elif voter_id == "O'Tooley":
        OTooley_vote_count = OTooley_vote_count + 1

print(f'Election Results')
print(f'-----------------')

#to find total votes cast
print(f'Total Votes: {len(voter_id)}')
print(f'-----------------')

# list of candidates who received votes
candidate_with_votes = set(candidates)
final_candidate_list = list(candidate_with_votes)
print(final_candidate_list)

# vote totals, percents

print(f'Khan : {(Khan_vote_count/len(voter_id)) * 100} ({Khan_vote_count})')
print(f'Li : {(Li_vote_count/len(voter_id)) * 100} ({Li_vote_count})')
print(f'Correy : {(Correy_vote_count/len(voter_id)) * 100} ({Correy_vote_count})')
print(f"O'Tooley : {(OTooley_vote_count/len(voter_id)) * 100} ({OTooley_vote_count})")

print(f'Winner : {max(candidate_with_votes)}')