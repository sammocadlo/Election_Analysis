# The data we need to retrieve

#add our dependencies 
import csv
import os

#assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#assign a variable to save the file to the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. initialize a total vote counter
total_votes = 0
#declare list of candidates
candidate_options = []
#declare an empty dictionary
candidate_votes = {}
#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    
    #print each row in the CSV file
    for row in file_reader:
        #2. add to the total vote count
        total_votes += 1
    #print the candidate name from each row
        candidate_name = row[2]

        #if the candidate does not match any existing candidate in the list...
        if candidate_name not in candidate_options:
        #add it to the list!
            candidate_options.append(candidate_name)
        #begin tracking the candidates vote count
            candidate_votes[candidate_name] = 0
        #add a vote to that candidates count
        candidate_votes[candidate_name] += 1

#determine % of votes for each candidate by looping through the counts
#iterate thru name list
for candidate_name in candidate_votes:
    #retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #calc % of votes
    vote_percentage = votes/total_votes * 100
    #print candidate name and % of votes

#to do - print each candidates name, vote count, and % to terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #determine if the votes are greater than the winning_count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true, set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #set winning_candidate = candidate_name
        winning_candidate = candidate_name

#to do - print the winning candidate, vote count, and % to terminal 
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n"
)
print(winning_candidate_summary)

# 1. The total number of votes cast - 369711 - X
# 2. A complete list of the candidates who received votes - X
# 3. The percentage of votes each candidate won - X
# 4. The total number of votes each candidate won - X
# 5. The winner of the election based on popular vote