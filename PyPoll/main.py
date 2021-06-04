import pathlib
import csv

election_data_csv = pathlib.Path("/Users/erinbabamoto/Desktop/USC_Bootcamp/Homework/python-challenge/PyPoll/Resources/election_data.csv")

with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    votes = {}

## A complete list of candidates who received votes
    for row in csvreader:
        candidate_name = row[2]
## The total number of votes each candidate won
        if candidate_name in votes:
            votes[candidate_name] += 1
        else:
            votes[candidate_name] = 1

    # print(votes)
    vote_counts = list(votes.values())

## The total number of votes cast
    total_count = sum(vote_counts)
    # print(total_count)

## The percentage of votes each candidate won
winner = list(votes.keys())[0]
votes_summary = {}
for candidate in votes.keys():
    if votes[candidate] > votes[winner]:
        winner = candidate
    votes_summary[candidate] = {"votes": votes[candidate], "vote_percentage": round((votes[candidate]/total_count)*100, 3)}
## The winner of the election based on popular vote
    if candidate == winner:
        votes_summary[candidate]["is winner"] = True
    else:
        votes_summary[candidate]["is winner"] = False


# export to text file
election_results_csv = pathlib.Path("/Users/erinbabamoto/Desktop/USC_Bootcamp/Homework/python-challenge/PyPoll/Analysis/election_results.txt")

with open(election_results_csv, "w") as outputfile:
    #csvwriter = csv.writer(outputfile)
        election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_count}\n"
        "-------------------------\n"
        )
        print(election_results, end="")

        outputfile.write(election_results)
        
        for candidate in votes_summary.keys():
            voter_output = f"{candidate}: {votes_summary[candidate]['vote_percentage']}% ({votes_summary[candidate]['votes']})\n"
            print(voter_output, end = "")

            outputfile.write(voter_output)

        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n"
        )

        outputfile.write(winning_candidate_summary)

        print(winning_candidate_summary)