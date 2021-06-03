'''
Main script for the PyPoll portion of HW3
Authored By: Merari Cisneros
'''

#Importing Dependencies
import os , csv , numpy as np , pprint as pp

#Read in PyPoll_Analysis.csv
file = os.path.join('PyPoll' , 'Resources' , 'PyPoll_Data.csv'); # Root file path is:  C:\Users\daypa\Documents\git\Python-Challenge

with open(file , 'r') as f:

    f_reader = csv.reader(f , delimiter = ',');

    header = next(f_reader); #storing the header

    Candidates = {}; #stores candidates
    Total_Votes = 0; #Counts rows/votes


    for vote in f_reader:

        Candidates.setdefault(vote[2] , [0,0]); # create a key for candidates as they are encountered

        Candidates[vote[2]][0] += 1; # Populate a candidates first list item with their vote_count
        
        Total_Votes += 1; #Keep track of the total rows/votes 


# Determining percent vote for each candidate

for candidate in Candidates:

    Candidate_Votes = Candidates[candidate][0]; # references the value where candidate specific vote count exists

    Candidates[candidate][1] = (Candidate_Votes / Total_Votes) * 100;


# Finding the value in the dictionary that is the largest

Max_Vote = max(Candidates.values());

#Associating the largest value with its dictionary key thus finding the weiner....er I mean winner.

for key , value in Candidates.items():

    if value == Max_Vote:
        Winner = key;

#Storing my Analysis strings as variables for easier printing

candidates_list = list(Candidates.items());

H = 'PyPoll Results';
L1 = f'The total number of votes is: {Total_Votes}';
L2 = f'The candidates are: (Candidate / Vote_Count / Vote_Percent) {candidates_list}';
L3 = f'The Winner is.....: {Winner}'
new_line = '\n';

Paragraph = [H , new_line ,  L1 , new_line ,  L2 , new_line ,  L3];

#Writing the results to the Pypoll_Results.txt

w_file = os.path.join('PyPoll' , 'Analysis' , 'PyPoll_Results.txt');

with open(w_file , 'w') as f2:

    f2.writelines(Paragraph);

#Printing results to the terminal

for i in Paragraph:
    pp.pprint(i);





