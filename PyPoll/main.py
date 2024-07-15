import pandas as pd

# Load the data
file_path = 'Resources/election_data.csv'
data = pd.read_csv(file_path)

# Calculate the total number of votes cast
total_votes = data.shape[0]

# Calculate the total number of votes each candidate won
candidate_votes = data['Candidate'].value_counts()

# Calculate the percentage of votes each candidate won
candidate_percentage = (candidate_votes / total_votes) * 100

# Determine the winner of the election based on popular vote
winner = candidate_votes.idxmax()
sorted_candidates = sorted(candidate_votes.index)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in sorted_candidates:
    print(f"{candidate}: {candidate_percentage[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open("analysis/pypoll_analysis.txt", "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate in sorted_candidates:
        file.write(f"{candidate}: {candidate_percentage[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")