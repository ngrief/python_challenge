# Import necessary libraries
import os
import pandas as pd
 
# Set the exact path to the CSV file
poll_path = r"c:\Users\ntrie\OneDrive\Desktop\Challenge 3\python_challenge\PyPoll\Resources\election_data.csv"
 
# Verify the file exists
if not os.path.exists(poll_path):
    print(f"Error: File not found at {poll_path}")
    exit()
 
# Read the CSV file into a pandas DataFrame
df = pd.read_csv(poll_path)
 
# Calculate total number of votes
total_votes = len(df)
 
# Count votes for each candidate
candidate_votes = df['Candidate'].value_counts()
 
# Calculate percentage of votes for each candidate
percentages = (candidate_votes / total_votes) * 100
 
# Find the winner
winner = candidate_votes.idxmax()
 
# Prepare the results string
results = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""
 
for candidate, votes in candidate_votes.items():
    results += f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n"
 
results += f"""-------------------------
Winner: {winner}
-------------------------
"""
 
# Print results to console
print(results)
 
# Create output directory if it doesn't exist
output_dir = os.path.join(os.path.dirname(poll_path), "..", "Analysis")
os.makedirs(output_dir, exist_ok=True)
 
# Write results to text file
output_path = os.path.join(output_dir, "election_results.txt")
with open(output_path, 'w') as output_file:
    output_file.write(results)
 
print(f"Results have been saved to {output_path}")