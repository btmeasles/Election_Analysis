# The data we need to recieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote



import csv
import os

#  Assign a variable for the file to load and the path.
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path
file_to_save=os.path.join("election_analysis.txt")
# 1. Initialize a total vote counter
total_votes=0
# Candidate options list creation/Candidate votes dictionary creation
candidate_options=[]
candidate_votes={}
# Winning Candidate and Winning Count Tracker
winning_candidate=""
winning_count=0
winning_percentage=0

with open(file_to_load) as election_data:
# To do: read and analyze the data here:::

    file_reader = csv.reader(election_data)
# Print each row in the CSV file
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name=row[2]
        # If the candidate name does not match any existing candidate....
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    election_results=(
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    
    for candidate_name in candidate_votes:
        votes=candidate_votes[candidate_name]
        vote_percentage=float(votes)/float(total_votes)*100
        candidate_results=(
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count=votes
            winning_candidate=candidate_name
            winning_percentage=vote_percentage

    winning_candidate_summary=(
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)




