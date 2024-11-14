# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}  # Dictionary to track candidate names and vote counts
winning_candidate = ""  # Track the winning candidate
winning_count = 0  # Track the winning vote count
winning_percentage = 0  # Track the winning vote percentage
# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes += 1  # Increment total votes
        candidate_name = row[2]
       
        
        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        # Add a vote to the candidate's count


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
   
    # Write the total vote count to the text file
    print(election_results, end="")
    txt_file.write(election_results)    

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_name, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100

        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name


        # Print and save each candidate's vote count and percentage

        candidate_results = f"{candidate_name}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results, end="")
        txt_file.write(candidate_results)

    # Generate and print the winning candidate summary
    winning_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
    )
    print(winning_summary)
    txt_file.write(winning_summary)

    # Save the winning candidate summary to the text file
