from sys import argv, exit
import csv

if len(argv) != 3:
    print("Usage: database.csv sequence.txt")
    exit(1)
    
Database = open(argv[1], "r")                 # Initalizing variable which reads second command line argument 
DNAsequence = open(argv[2], "r")              # Initalizing variable which reads third command line argument

data = csv.reader(Database) # Initalizing variable which reads second command line argument file
DATAsequences = csv.reader(DNAsequence) # Initalizing variable which reads third command line argument file

FirstParameterRow = []
sequence = []
value = []
STRdictonary = {}

i = 0

for row in data:                            
    if i == 0:
        FirstParameterRow = row.copy() 
    else:
        STRdictonary[row[0]] = row.copy()
        STRdictonary[row[0]].pop(0)
    i = 1

for row in DATAsequences: #Copy the data from the Datasequences file row by row                             
    sequence = row.copy()
    DATAsequences = sequence[0] # Make the first row in the sequences list equal to the Datasequences for confirmation
    sequence.clear() #Clear the sequences list of is data

for j in range(1, len(FirstParameterRow)):
    reps = FirstParameterRow[j] # Find the repititions of the STR patterns (not includiing the "names" parameter) within the DATAsequences file
    maximum = 0 #initilaze a counter foor the max amount of reps in DATAsequences file
    while DATAsequences.count(reps) > 0:
        maximum += 1
        reps += FirstParameterRow[j]
    value.append(str(maximum)) # Insert data of maximum STR patterns within the table for later use

for key in STRdictonary:
    if STRdictonary[key] == value:
        print(key)
        exit(0)

print("No match")
Database.close() # Close both of the files
DNAsequence.close()