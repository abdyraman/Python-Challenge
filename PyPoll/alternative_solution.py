import csv


#Defining the pathes to read csv files
read_filepath= "/Users/zhibekabdyramanova/Documents/GitHub/Python-Challenge/PyPoll/Resources/election_data.csv"

#creating the lists based on the data
ballotid=[]
county=[]
candidate={}
#candidate=[]

#opening the file to read the lists
with open(read_filepath, "r") as f:
    reader= csv.reader(f, delimiter=",")

     # Read the header row first (skip this part if there is no header)
    csv_header = next(f)
    #print(f"Header: {csv_header}") to check that headers are not taken into account

    for row in reader:
          # print(row[0], row[1], row[2]) 
        ballotid.append(int(row[0]))
        county.append (row[1])
        try:
            candidate[row[2]]+=1
            # candidate[row[2]][row[1]]+=1
            # candidate[row[2]]["Total"]+=1
        except:
            candidate[row[2]]=1
            # candidate[row[2]]={}
            # candidate[row[2]][row[1]]=1
            # candidate[row[2]]["Total"]=1
        
        # if row[2] not in candidate:
        #     candidate.append(row[2])
print(candidate)

my_dict = {}

#A complete list of candidates who received votes
non_repeating_names = list(set(candidate))
print(non_repeating_names)

# append the list to the dictionary
my_dict['Raymon Anthony Doane', 'Charles Casper Stockham', 'Diana DeGette'] = candidate

# print the dictionary
#print(my_dict)