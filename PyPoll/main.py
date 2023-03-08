import csv


#Defining the pathes to read and write in csv files
read_filepath= "/Users/zhibekabdyramanova/Documents/GitHub/Python-Challenge/PyPoll/Resources/election_data.csv"
write_filepath= "/Users/zhibekabdyramanova/Documents/GitHub/Python-Challenge/PyPoll/Resources/processed_election_data.csv"

#creating the lists based on the data
ballotid=[]
county=[]
candidate=[]
vote_count=0

#opening the file to read the lists
with open(read_filepath, "r") as f:
    reader= csv.reader(f, delimiter=",")

     # Read the header row first (skip this part if there is no header)
    csv_header = next(f)
    #print(f"Header: {csv_header}") to check that headers are not taken into account

    for row in reader:
       # print(row[0], row[1], row[2]) just to check if filepath is correct
        ballotid.append(int(row[0]))
        county.append (row[1])
        candidate.append(row[2])

#The total number of votes cast
print(len(ballotid))

#A complete list of candidates who received votes
non_repeating_names = list(set(candidate))
print(non_repeating_names)


# #The total number of votes each candidate won

count_rad = candidate.count('Raymon Anthony Doane')
print(count_rad)  

count_ccs = candidate.count('Charles Casper Stockham')
print(count_ccs)  

count_dd = candidate.count('Diana DeGette')
print(count_dd)  

Total= count_rad+count_dd+count_ccs
print(Total)

#The percentage of votes each candidate won

first_candidate=(count_rad/Total)*100
second_candidate=(count_ccs/Total)*100
third_candidate=(count_dd/Total)*100
print("%d%%" %first_candidate)
print("%d%%" %second_candidate)
print("%d%%" %third_candidate)

#The winner of the election based on popular vote
def popular_vote(candidates):
    # A dictionary to store the vote count for each candidate
    vote_count = {}
    for candidate in candidates:
        if candidate in vote_count:
            vote_count[candidate] += 1
        else:
            vote_count[candidate] = 1
    
    # Find the candidate with the most votes
    max_votes = 0
    winner = None
    for candidate, votes in vote_count.items():
        if votes > max_votes:
            max_votes = votes
            winner = candidate
    
    return winner

popular_vote(candidate)
