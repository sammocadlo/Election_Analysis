# The data we need to retrieve

#add our dependencies 
import csv
import os

#assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#assign a variable to save the file to the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    print(headers)

#use the with statement to open the file as a text file
    with open(file_to_save, "w") as txt_file:

#write three counties to the file
        txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")



# 1. The total number of votes cast
# 2. A complete list of the candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote