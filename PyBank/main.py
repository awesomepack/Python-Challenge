''' 
PyBank Main Script
Authored by: Merari Cisneros

* Read Financial data from CSV source
'''
#Importing dependencies
import os , csv
from typing import NewType

from numpy import average

# Reading the PyBank CSV
file = os.path.join('PyBank' , 'Resources' , 'PyBank.csv'); # "C:\Users\daypa\Documents\git\Python-Challenge" The path I started from.

with open(file , 'r') as Fdata:

    Fdata_reader = csv.reader(Fdata  , delimiter = ',');

    header = next(Fdata_reader); # skips the header row


    Months = []; #stores dates
    PL = []; #stores profit/loss info

    for row in Fdata_reader:

        Months.append(row[0]);
        PL.append(int(row[1]));


#Determining Time Span of datasets (Months)

Total_Months = len(Months);

#Net Total Profit/Loss ($)

Net_Total = sum(PL); # The net total is simply the sum of our profit/loss values in the data set.

#Computing average change in PL

change = []; #Stores value change info

for i in range(1 , len(PL)):

    Prev_Value = PL[i - 1]; #Previoys value in PL
    Curr_Value = PL[i]; #Current value in PL
    change.append(Curr_Value - Prev_Value);

avg_change = average(change); #Computing average from change

# Finding the max and min values in change list

Increase = max(change);
Decrease = min(change);

#Writing results to txt file

w_file = os.path.join('PyBank' , 'Analysis' , 'PyBank_Analysis.txt');

Header = '==========PyBank Report==========';
L1 = f'The total number of months is {Total_Months}';
L2 = f'The Total is {Net_Total}';
L3 = f'The average change is {avg_change}';
L4 = f'Greatest Increase: {Increase}';
L5 = f'Greatest Decrease: {Decrease}'; 
new_line = '\n';

Report = [Header , new_line , L1 , new_line , L2 , new_line , L3 , new_line , L4 , new_line , L5];

with open(w_file , 'w') as f:

    f.writelines(Report);

    


