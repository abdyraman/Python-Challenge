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
    print(f"Header: {csv_header}")

    for row in reader:
        #print(row[0], row[1]) just to check if filepath is correct
        date.append(row[0])
        proflosses.append (int(row[1]))

#Total months
print (len(date))

#Total Profits losses
print (sum(proflosses))

#Average Change
# def average(numbers):
#     length = len(numbers)
#     total = 0.0
#     for number in numbers:
#         total += number
#     return total / length

# print(average(proflosses))



#Greatest increase in profits
max_value = max(proflosses)
print(max_value)

#Greatest decrease in profits
min_value = min(proflosses)
print(min_value)
