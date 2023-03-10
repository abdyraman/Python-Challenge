import csv

#Defining the path to read csv file
read_filepath= "/Users/zhibekabdyramanova/Documents/GitHub/Python-Challenge/PyPoll/Resources/election_data.csv"

#creating the lists and values based on the data
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

#Creating txt file
file = open("PyPoll/Analysis/results.txt", "w")

#The total number of votes cast
print("Election Results")
print("-------------------------")
print("Total Votes: ", end= "") 
print(len(ballotid))
print("-------------------------")

#Adding value to txt
file.write("Election Results"+ "\n")
file.write("-------------------------"+ "\n")
file.write("Total Votes:"+ "\n") 
file.write(str(len(ballotid))+ "\n") #why str works, and int doesnt?
file.write("-------------------------"+ "\n")

#A complete list of candidates who received votes
non_repeating_names = list(set(candidate))
print(non_repeating_names)

#The total number of votes each candidate won
count_rad = candidate.count('Raymon Anthony Doane')
count_ccs = candidate.count('Charles Casper Stockham')
count_dd = candidate.count('Diana DeGette')

Total= count_rad+count_dd+count_ccs

#The percentage of votes each candidate won
first_candidate=(count_rad/Total)*100
second_candidate=(count_ccs/Total)*100
third_candidate=(count_dd/Total)*100

print("Raymon Anthony Doane: "+"%d%%" %first_candidate + "  ", end= "") 
print(count_rad)
print("Charles Casper Stockham: "+"%d%%" %second_candidate + "  ", end= "") 
print(count_ccs) 
print("Diana DeGette: "+ "%d%%" %third_candidate + "  ", end= "") 
print(count_dd)  

#Adding text to the txt file
file.write("Raymon Anthony Doane:{}%\n".format(first_candidate))
file.write (str(count_rad))
file.write("\n")
file.write("Charles Casper Stockham:{}%\n".format(second_candidate)) 
file.write(str(count_ccs)) 
file.write("\n")
file.write("Diana DeGette:{}%\n".format(third_candidate)) 
file.write(str(count_dd))  
file.write("\n")

#The winner of the election based on popular vote
def popular_vote(candidates):

    # A dictionary to store the vote count for each candidate
    vote_count = {}
    for candidate in candidates:
        if candidate in vote_count.keys():
            vote_count[candidate] += 1
        else:
            vote_count[candidate] = 1
    
    # Find the candidate with the most votes
    max_votes = 0
    for candidate, votes in vote_count.items():
        if votes > max_votes:
            max_votes = votes
            winner = candidate
    
    return winner
print("-------------------------")
print("Winner:"+ popular_vote(candidate))
print("-------------------------")

#Adding to txt
file.write("-------------------------"+ "\n")
file.write("Winner:"+ popular_vote(candidate) + "\n")
file.write("-------------------------" + "\n")


file.close()