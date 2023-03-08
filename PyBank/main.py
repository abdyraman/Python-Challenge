import csv

#Defining the pathes to read and write in csv files
read_filepath= "/Users/zhibekabdyramanova/Documents/GitHub/Python-Challenge/PyBank/Resources/budget_data.csv"
write_filepath= "/Users/zhibekabdyramanova/Documents/GitHub/Python-Challenge/PyBank/Resources/processed_budget_data.csv"

#creating the lists based on the data
date=[]
proflosses=[]

#opening the file to read the lists
with open(read_filepath, "r") as f:
    reader= csv.reader(f, delimiter=",")

 # Read the header row first (skip this part if there is no header)
    csv_header = next(f)
    #print(f"Header: {csv_header}")

    for row in reader:
        #print(row[0], row[1]) just to check if filepath is correct
        date.append(row[0])
        proflosses.append (int(row[1]))

#Total months
print (len(date))

#Total Profits losses
print (sum(proflosses))

#Average Change
for i in range (len(proflosses)-1):
    difference= [proflosses[i+1]-(proflosses[i])]
    print(difference)

ave= sum(difference)/len(difference)
print(ave)

#Average difference

def average_change(data):
    diff=[data[i+1]-data[i] for i in range(len(data)-1)]
    ave_chan=sum(diff)/len(diff)
    return ave_chan

average_change(proflosses)
print("ave_chan")


# print(average(proflosses))



#Greatest increase in profits
# max_value = max(proflosses)
# print(max_value)

#Greatest decrease in profits
#min_value = min(proflosses)
#print(min_value)
