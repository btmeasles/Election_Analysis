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
# Candidate options list creation
candidate_options=[]
with open(file_to_load) as election_data:
# To do: read and analyze the data here:::

    file_reader = csv.reader(election_data)
# Print each row in the CSV file
    headers = next(file_reader)
    for row in file_reader:
        total_votes +=1
        candidate_name=row[2]
        # If the candidate name does not match any existing candidate....
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

# 3. Print the total votes
print(candidate_options)
print(total_votes)



