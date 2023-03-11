import csv

#Defining the pathes to read csv file
read_filepath= "/Users/zhibekabdyramanova/Documents/GitHub/Python-Challenge/PyBank/Resources/budget_data.csv"

#creating the lists and values based on the data
date=[]
proflosses=[]
net_total=0
pl_change=[]
average_change=0

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
        net_total+= int(row[1])

print("Financial Analysis")
print("----------------------------")
#Total months
print ("Total Months: ", end="")
print (len(date))

#Total Profits losses
print ("Total: ", end="")
print (sum(proflosses))

#Creation of txt document
file = open("PyBank/Analysis/results.txt", "w")

#Adding values to txt
file.write("Financial Analysis"+ "\n")
file.write("----------------------------"+ "\n")
file.write("Total Months: ")
file.write(str(len(date))+ "\n")
file.write("Total: ")
file.write(str(sum(proflosses))+ "\n")

#Looping through the profits and losses to make a list of changes (i+1)-(i)
for i in range (len(proflosses)-1):
    pl_change.append(proflosses[i+1]-proflosses[i])

#Greatest increase in profits
print ("Greatest decrease in profits: ", end="")
print(max(pl_change))

max_value = (max(pl_change))
#+1 because the value is starting from the second row (2-1)
max_index = pl_change.index(max_value)+1
matching_value = date[max_index]
print(matching_value)

#Adding value to txt
file.write("Greatest increase in profits: ")
file.write(str(max(pl_change))+"\n")
file.write(str(matching_value)+"\n")

#Greatest decrease in profits
print ("Greatest decrease in profits: ", end="")
print(min(pl_change))

min_value=(min(pl_change))
#+1 because the value is starting from the second row (2-1)
min_index = pl_change.index(min_value)+1
matching_value = date[min_index]
print(matching_value)

#Adding value to txt
file.write("Greatest decrease in profits: ")
file.write(str(min(pl_change))+"\n")
file.write(str(matching_value)+"\n")

#Average Change
for i in range (len(pl_change)):
    average_change += pl_change[i]

average_change= average_change/len(pl_change)
print ("Average Change: ", end="")
print(average_change)

#Adding value to txt
file.write("Average Change: ")
file.write(str(average_change))

#Closing txt
file.close()