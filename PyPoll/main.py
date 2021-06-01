'''
Main script for the PyPoll portion of HW3
Authored By: Merari Cisneros
'''

#Importing Dependencies
import os , csv , numpy as np

#Read in PyPoll_Analysis.csv
file = os.path.join('PyPoll' , 'Resources' , 'PyPoll_Data.csv'); # Root file path is:  C:\Users\daypa\Documents\git\Python-Challenge

with open(file , 'r') as f:

    f_reader = csv.reader(f , delimiter = ',');

    header = next(f_reader); #skipping the header

    Candidates = {}; #stores candidates
    Total_Votes = 0; #Counts rows


    for vote in f_reader:

        Candidates.setdefault(vote[2] , [0,0]); 

        Candidates[vote[2]][0] += 1;
        
        Total_Votes += 1;


# Determining the Total Number of Votes

print(f'The Total Number of Votes is {Total_Votes}');


# Determining percent vote for each candidate

for candidate in Candidates:

    Candidate_Votes = Candidates[candidate][0];

    Candidates[candidate][1] = (Candidate_Votes / Total_Votes) * 100;


print(Candidates['Khan']);

#Determine the winner by vote count and print their name.