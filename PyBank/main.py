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

    for row in reader:
        #print(row[0], row[1]) just to check if filepath is correct
        date.append(row[0])
        proflosses.append(row[1])
print (len(date))

