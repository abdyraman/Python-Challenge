import csv

#Defining the pathes to read and write in csv files
read_filepath= "/Users/zhibekabdyramanova/Documents/GitHub/Python-Challenge/PyPoll/Resources/election_data.csv"
write_filepath= "/Users/zhibekabdyramanova/Documents/GitHub/Python-Challenge/PyPoll/Resources/processed_election_data.csv"

#creating the lists based on the data
ballotid=[]
county=[]
candidate=[]

#opening the file to read the lists
with open(read_filepath, "r") as f:
    reader= csv.reader(f, delimiter=",")

     # Read the header row first (skip this part if there is no header)
    csv_header = next(f)
    print(f"Header: {csv_header}")

    for row in reader:
       # print(row[0], row[1], row[2]) just to check if filepath is correct
        ballotid.append(int(row[0]))
        county.append (row[1])
        candidate.append(row[2])
print(candidate)