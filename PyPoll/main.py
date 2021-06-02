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

    header = next(f_reader); #skipping the header

    Candidates = {}; #stores candidates
    Total_Votes = 0; #Counts rows


    for vote in f_reader:

        Candidates.setdefault(vote[2] , [0,0]); 

        Candidates[vote[2]][0] += 1;
        
        Total_Votes += 1;




# Determining percent vote for each candidate

for candidate in Candidates:

    Candidate_Votes = Candidates[candidate][0];

    Candidates[candidate][1] = (Candidate_Votes / Total_Votes) * 100;


pp.pprint(Candidates);

# Finding the value in the dictionary that is the largest

Max_Vote = max(Candidates.values());

#Associating the largest value with its dictionary key thus finding the weiner....er I mean winner.

for key , value in Candidates.items():

    if value == Max_Vote:
        Winner = key;

#Storing my Analysis strings as variables

H = 'PyPoll Results';

L1 = f'The total number of votes is: {Total_Votes}';
L2 = f'The candidates are:{Candidates.items()}';
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





